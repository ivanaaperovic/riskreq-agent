"""
data_processing.py
------------------
OBRADA ULAZNIH PODATAKA pre slanja modelu (zahtev: vise koraka obrade).

Agent prima opis projekta / funkcionalnosti iz tri moguca izvora:
  1) direktan unos sa terminala,
  2) tekstualni fajl iz foldera 'ulaz/',
  3) (opciono) ziva CreatorLab WooCommerce prodavnica preko REST API-ja.

U svim slucajevima ulaz se PRIPREMA pre LLM-a:
- ciscenje HTML tagova / entiteta (kod WooCommerce opisa),
- sazimanje viska praznina,
- skracivanje (chunking) preduugackog teksta da ne trosimo previse tokena.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Maksimalna duzina teksta (u karakterima) koji saljemo modelu.
MAX_ULAZ_LEN = 4000
# Maksimalna duzina opisa po proizvodu (kad se cita WooCommerce prodavnica).
MAX_OPIS_LEN = 600

ULAZ_DIR = Path(__file__).parent / "ulaz"


# ----------------------------------------------------------------------
# Ciscenje i skracivanje teksta
# ----------------------------------------------------------------------
def ocisti_html(tekst: str) -> str:
    """Ukloni HTML tagove i dekoduj HTML entitete (&amp; -> &)."""
    if not tekst:
        return ""
    bez_tagova = re.sub(r"<[^>]+>", " ", tekst)
    dekodovano = html.unescape(bez_tagova)
    return re.sub(r"[ \t]+", " ", dekodovano).strip()


def skrati(tekst: str, maks: int = MAX_ULAZ_LEN) -> str:
    """Skrati preduugacki tekst (chunking) na granicu recenice."""
    if len(tekst) <= maks:
        return tekst
    odsecak = tekst[:maks]
    tacka = odsecak.rfind(". ")
    if tacka > maks * 0.5:
        return odsecak[: tacka + 1] + "\n[...tekst skracen...]"
    return odsecak.rstrip() + " [...tekst skracen...]"


def pripremi_ulaz(tekst: str) -> str:
    """Glavna priprema slobodnog teksta: ocisti praznine + skrati."""
    sredjeno = re.sub(r"\n{3,}", "\n\n", tekst.strip())
    return skrati(sredjeno)


# ----------------------------------------------------------------------
# Izvor 1/2: fajl iz foldera 'ulaz/'
# ----------------------------------------------------------------------
def listaj_ulazne_fajlove() -> list[Path]:
    """Vrati .txt / .md fajlove iz foldera 'ulaz/'."""
    if not ULAZ_DIR.exists():
        return []
    fajlovi = sorted(
        p for p in ULAZ_DIR.iterdir() if p.suffix.lower() in {".txt", ".md"}
    )
    return fajlovi


def ucitaj_fajl(putanja: Path) -> str:
    """Ucitaj i pripremi sadrzaj tekstualnog fajla."""
    tekst = putanja.read_text(encoding="utf-8")
    return pripremi_ulaz(tekst)


# ----------------------------------------------------------------------
# Izvor 3 (opciono): WooCommerce prodavnica (CreatorLab e-commerce app)
# ----------------------------------------------------------------------
@dataclass
class Proizvod:
    """Normalizovan, ocisten prikaz jednog proizvoda iz prodavnice."""

    id: int
    naziv: str
    cena: str
    opis: str
    kategorije: list[str]

    @property
    def cena_broj(self) -> float:
        try:
            return float(self.cena)
        except (ValueError, TypeError):
            return 0.0


def normalizuj_proizvode(sirovi: list[dict[str, Any]]) -> list[Proizvod]:
    """Pretvori sirovi WooCommerce JSON u listu ociscenih Proizvod objekata."""
    proizvodi: list[Proizvod] = []
    for p in sirovi:
        if p.get("status") and p.get("status") != "publish":
            continue
        opis_izvor = p.get("short_description") or p.get("description") or ""
        opis = ocisti_html(opis_izvor)[:MAX_OPIS_LEN]
        proizvodi.append(
            Proizvod(
                id=int(p.get("id", 0)),
                naziv=ocisti_html(p.get("name", "Nepoznat proizvod")),
                cena=str(p.get("price") or p.get("regular_price") or "0"),
                opis=opis or "(nema opisa)",
                kategorije=[c.get("name", "") for c in p.get("categories", [])],
            )
        )
    proizvodi.sort(key=lambda k: k.cena_broj)
    return proizvodi


def prodavnica_kao_opis(proizvodi: list[Proizvod]) -> str:
    """
    Formatira ucitanu prodavnicu u tekstualni opis sistema koji se analizira.
    Taj opis postaje ULAZ za analizu zahteva / rizika CreatorLab aplikacije.
    """
    if not proizvodi:
        return "(prodavnica je prazna)"
    linije = [
        "CreatorLab je e-commerce (WooCommerce) aplikacija - online akademija koja "
        "prodaje onlajn kurseve. Trenutni katalog proizvoda dovucen sa zive prodavnice:",
        "",
    ]
    for k in proizvodi:
        kat = ", ".join(c for c in k.kategorije if c) or "bez kategorije"
        linije.append(
            f"- [{k.id}] {k.naziv} | cena: {k.cena} EUR | kategorija: {kat}\n"
            f"    Opis: {k.opis}"
        )
    return pripremi_ulaz("\n".join(linije))
