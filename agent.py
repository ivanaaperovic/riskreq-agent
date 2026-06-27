"""
agent.py
--------
AI LOGIKA AGENTA - visekoracni workflow (zahtev: min. 2-3 koraka + LLM komponenta).

Agent NIJE chatbot: za jedan ulaz izvrsava lanac od 3 LLM koraka, gde izlaz
svakog koraka ulazi u sledeci, i na kraju vraca strukturisan Markdown izlaz.

Rezimi:
- analiza_zahteva():  A1 akteri/celine -> A2 user stories -> A3 kriterijumi
- registar_rizika():  B1 komponente   -> B2 rizici       -> B3 procena/registar
"""

from __future__ import annotations

from typing import Callable

from langchain_core.output_parsers import StrOutputParser

from config import Settings
from llm_provider import kreiraj_llm
from prompts import (
    A1_AKTERI_PROMPT,
    A2_USER_STORIES_PROMPT,
    A3_KRITERIJUMI_PROMPT,
    B1_KOMPONENTE_PROMPT,
    B2_IDENTIFIKACIJA_PROMPT,
    B3_PROCENA_PROMPT,
)


class AgentError(Exception):
    """Greska tokom poziva LLM-a."""


# Tip za callback kojim main.py prikazuje napredak po koracima.
Napredak = Callable[[str], None]


class RizikZahteviAgent:
    """AI agent za analizu zahteva i procenu rizika softverskog projekta."""

    def __init__(self, settings: Settings, model_override: str | None = None):
        self.settings = settings
        self.model_naziv = model_override or (
            settings.openai_model
            if settings.llm_provider == "openai"
            else settings.ollama_model
        )
        self._llm = kreiraj_llm(settings, model_override)
        self._parser = StrOutputParser()

    # ------------------------------------------------------------------
    # REZIM A: ANALIZA ZAHTEVA (3 koraka)
    # ------------------------------------------------------------------
    def analiza_zahteva(self, opis: str, napredak: Napredak = lambda s: None) -> str:
        napredak("Korak 1/3: izdvajam aktere i funkcionalne celine...")
        akteri_celine = self._korak(A1_AKTERI_PROMPT, {"opis": opis})

        napredak("Korak 2/3: generisem user stories...")
        user_stories = self._korak(
            A2_USER_STORIES_PROMPT,
            {"akteri_celine": akteri_celine, "opis": opis},
        )

        napredak("Korak 3/3: dodajem acceptance criteria i nefunkcionalne zahteve...")
        finalno = self._korak(
            A3_KRITERIJUMI_PROMPT, {"user_stories": user_stories}
        )

        return self._sastavi(
            naslov="Analiza zahteva",
            sekcije=[
                ("Korak 1 — Akteri i funkcionalne celine", akteri_celine),
                ("Korak 2 — User stories", user_stories),
                ("Korak 3 — Acceptance criteria i nefunkcionalni zahtevi", finalno),
            ],
        )

    # ------------------------------------------------------------------
    # REZIM B: REGISTAR RIZIKA (3 koraka)
    # ------------------------------------------------------------------
    def registar_rizika(self, opis: str, napredak: Napredak = lambda s: None) -> str:
        napredak("Korak 1/3: izdvajam kljucne komponente i resurse...")
        komponente = self._korak(B1_KOMPONENTE_PROMPT, {"opis": opis})

        napredak("Korak 2/3: identifikujem rizike po komponenti...")
        rizici = self._korak(
            B2_IDENTIFIKACIJA_PROMPT, {"komponente": komponente, "opis": opis}
        )

        napredak("Korak 3/3: procenjujem rizike i predlazem mere...")
        registar = self._korak(B3_PROCENA_PROMPT, {"rizici": rizici})

        return self._sastavi(
            naslov="Procena rizika",
            sekcije=[
                ("Korak 1 — Kljucne komponente i resursi", komponente),
                ("Korak 2 — Identifikovani rizici", rizici),
                ("Korak 3 — Registar rizika i prioriteti", registar),
            ],
        )

    # ------------------------------------------------------------------
    # Pomocne metode
    # ------------------------------------------------------------------
    def _korak(self, prompt, ulaz: dict) -> str:
        """Jedan korak workflow-a: prompt | model | parser."""
        lanac = prompt | self._llm | self._parser
        return self._pozovi(lanac, ulaz)

    @staticmethod
    def _sastavi(naslov: str, sekcije: list[tuple[str, str]]) -> str:
        """Spoji medjurezultate u jedan strukturisan Markdown dokument."""
        delovi = [f"# {naslov}\n"]
        for podnaslov, sadrzaj in sekcije:
            delovi.append(f"## {podnaslov}\n\n{sadrzaj.strip()}\n")
        return "\n".join(delovi)

    def _pozovi(self, lanac, ulaz: dict) -> str:
        try:
            return lanac.invoke(ulaz)
        except Exception as exc:
            poruka = str(exc).lower()
            if "api key" in poruka or "authentication" in poruka or "401" in poruka:
                raise AgentError(
                    "LLM je odbio kljuc. Proveri OPENAI_API_KEY u .env."
                ) from exc
            if "rate limit" in poruka or "429" in poruka:
                raise AgentError(
                    "Dostignut limit zahteva ka modelu. Sacekaj malo pa probaj ponovo."
                ) from exc
            if "timeout" in poruka or "timed out" in poruka:
                raise AgentError(
                    "Model nije odgovorio na vreme (timeout). "
                    "Povecaj REQUEST_TIMEOUT u .env ili probaj ponovo."
                ) from exc
            if "connection" in poruka or "connect" in poruka:
                raise AgentError(
                    "Ne mogu da se povezem na model. "
                    "Ako koristis Ollama, proveri da li je servis pokrenut."
                ) from exc
            raise AgentError(f"Greska pri pozivu modela: {exc}") from exc
