"""
config.py
---------
Centralno mesto za ucitavanje konfiguracije iz .env fajla.

Zahtevi koje pokriva (Grupa III):
- Koriscenje .env fajla i python-dotenv (API kljucevi nisu hardkodovani).
- Podrska za vise provajdera i vise modela (Ollama + OpenAI).

WooCommerce kljucevi su OPCIONI - potrebni su samo ako se kao ulaz bira
"povuci CreatorLab prodavnicu". Tekstualni / fajl ulaz radi i bez njih.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Ucitaj promenljive iz .env fajla u okruzenje.
load_dotenv()


class ConfigError(Exception):
    """Greska u konfiguraciji (npr. nedostaje obavezan podatak)."""


# Lista modela koje aplikacija nudi po provajderu (napredni zahtev: vise modela).
AVAILABLE_MODELS = {
    "openai": ["gpt-4o-mini", "gpt-4o", "gpt-4.1-mini"],
    "ollama": ["llama3.2", "llama3.1", "mistral", "qwen2.5"],
}


@dataclass
class Settings:
    """Sve podesavanja aplikacije na jednom mestu."""

    llm_provider: str
    openai_api_key: str
    openai_model: str
    ollama_model: str
    ollama_base_url: str
    wc_url: str
    wc_consumer_key: str
    wc_consumer_secret: str
    request_timeout: int
    llm_temperature: float

    @property
    def woocommerce_dostupan(self) -> bool:
        """True ako su WooCommerce kljucevi popunjeni (opcioni izvor podataka)."""
        return bool(self.wc_consumer_key and self.wc_consumer_secret)


def _get(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def load_settings() -> Settings:
    """Ucita i validira konfiguraciju iz okruzenja."""
    provider = _get("LLM_PROVIDER", "openai").lower()
    if provider not in AVAILABLE_MODELS:
        raise ConfigError(
            f"Nepoznat LLM_PROVIDER '{provider}'. "
            f"Dozvoljeno: {', '.join(AVAILABLE_MODELS)}."
        )

    try:
        timeout = int(_get("REQUEST_TIMEOUT", "60"))
    except ValueError:
        timeout = 60
    try:
        temperature = float(_get("LLM_TEMPERATURE", "0.4"))
    except ValueError:
        temperature = 0.4

    settings = Settings(
        llm_provider=provider,
        openai_api_key=_get("OPENAI_API_KEY"),
        openai_model=_get("OPENAI_MODEL", "gpt-4o-mini"),
        ollama_model=_get("OLLAMA_MODEL", "llama3.1"),
        ollama_base_url=_get("OLLAMA_BASE_URL", "http://localhost:11434"),
        wc_url=_get("WC_URL", "http://localhost:8080"),
        wc_consumer_key=_get("WC_CONSUMER_KEY"),
        wc_consumer_secret=_get("WC_CONSUMER_SECRET"),
        request_timeout=timeout,
        llm_temperature=temperature,
    )

    _validate(settings)
    return settings


def _validate(s: Settings) -> None:
    """Proveri da li su OBAVEZNI podaci prisutni (samo LLM provajder)."""
    if s.llm_provider == "openai":
        if not s.openai_api_key or s.openai_api_key.startswith("sk-zameni"):
            raise ConfigError(
                "Nije postavljen pravi OPENAI_API_KEY u .env fajlu.\n"
                "   Otvori .env i upisi svoj kljuc (pocinje sa 'sk-'),\n"
                "   ili predji na lokalni model: LLM_PROVIDER=ollama."
            )
    # WooCommerce kljucevi NISU obavezni - proverava ih woocommerce_client
    # tek ako korisnik izabere taj izvor podataka.
