"""
llm_provider.py
---------------
Fabrika za LLM modele - PODRSKA ZA VISE PROVAJDERA I MODELA (napredni zahtev).

Vraca LangChain chat model na osnovu provajdera iz konfiguracije:
- "openai" -> ChatOpenAI (vise modela: gpt-4o-mini, gpt-4o, ...)
- "ollama" -> ChatOllama (lokalni modeli; ukljucuje se jednom linijom)

Zahvaljujuci ovoj apstrakciji, ostatak aplikacije ne zna (i ne mora da zna)
koji se konkretno model koristi.
"""

from __future__ import annotations

from config import ConfigError, Settings


def kreiraj_llm(settings: Settings, model_override: str | None = None):
    """
    Napravi i vrati LangChain chat model.

    model_override: ako je zadat, koristi taj model umesto onog iz .env
                    (koristi se kad korisnik izabere model u meniju).
    """
    provider = settings.llm_provider

    if provider == "openai":
        try:
            from langchain_openai import ChatOpenAI
        except ImportError as exc:
            raise ConfigError(
                "Nedostaje paket 'langchain-openai'. Pokreni: pip install langchain-openai"
            ) from exc

        return ChatOpenAI(
            model=model_override or settings.openai_model,
            api_key=settings.openai_api_key,
            temperature=settings.llm_temperature,
            timeout=settings.request_timeout,
            max_retries=2,
        )

    if provider == "ollama":
        try:
            from langchain_ollama import ChatOllama
        except ImportError as exc:
            raise ConfigError(
                "Za Ollama provajder instaliraj: pip install langchain-ollama\n"
                "   (i pokreni lokalni Ollama server)."
            ) from exc

        return ChatOllama(
            model=model_override or settings.ollama_model,
            base_url=settings.ollama_base_url,
            temperature=settings.llm_temperature,
        )

    raise ConfigError(f"Nepodrzan provajder: {provider}")
