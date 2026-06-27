"""
main.py
-------
ULAZNA TACKA APLIKACIJE.

AI agent za podrsku project manager-u / product owner-u u razvoju softvera:
  1) Analiza zahteva   - iz opisa sistema generise user stories + acceptance criteria
  2) Registar rizika   - iz opisa sistema generise procenu rizika + mere ublazavanja

Tok rada (workflow):
  konfiguracija -> izbor modela -> izbor IZVORA ULAZA
  -> priprema/obrada ulaza -> visekoracni LLM agent
  -> strukturisan Markdown izlaz (prikaz + cuvanje u 'izlaz/').

Izvori ulaza:
  a) direktan unos teksta,
  b) tekstualni fajl iz foldera 'ulaz/',
  c) (opciono) ziva CreatorLab WooCommerce prodavnica.

Pokretanje:  python main.py
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from agent import AgentError, RizikZahteviAgent
from config import AVAILABLE_MODELS, ConfigError, load_settings
from data_processing import (
    listaj_ulazne_fajlove,
    pripremi_ulaz,
    prodavnica_kao_opis,
    normalizuj_proizvode,
    ucitaj_fajl,
)
from woocommerce_client import WooCommerceClient, WooCommerceError

IZLAZ_DIR = Path(__file__).parent / "izlaz"


# ----------------------------------------------------------------------
# Pomocne funkcije za unos / ispis
# ----------------------------------------------------------------------
def naslov(tekst: str) -> None:
    print("\n" + "=" * 60)
    print(f" {tekst}")
    print("=" * 60)


def unos(poruka: str) -> str:
    try:
        return input(poruka).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nPrekinuto. Dovidjenja!")
        sys.exit(0)


def napredak(poruka: str) -> None:
    """Callback koji agent zove izmedju koraka workflow-a."""
    print(f"  > {poruka}")


def izaberi_model(settings) -> str | None:
    modeli = AVAILABLE_MODELS.get(settings.llm_provider, [])
    podrazumevani = (
        settings.openai_model
        if settings.llm_provider == "openai"
        else settings.ollama_model
    )
    print(f"\nProvajder: {settings.llm_provider}")
    print("Dostupni modeli:")
    for i, m in enumerate(modeli, 1):
        oznaka = "  (podrazumevani)" if m == podrazumevani else ""
        print(f"  {i}) {m}{oznaka}")
    izbor = unos("Izaberi model [Enter = podrazumevani]: ")
    if not izbor:
        return None
    if izbor.isdigit() and 1 <= int(izbor) <= len(modeli):
        return modeli[int(izbor) - 1]
    return izbor


def sacuvaj_izlaz(sadrzaj: str, prefiks: str) -> Path:
    IZLAZ_DIR.mkdir(exist_ok=True)
    vreme = datetime.now().strftime("%Y%m%d_%H%M%S")
    putanja = IZLAZ_DIR / f"{prefiks}_{vreme}.md"
    putanja.write_text(sadrzaj, encoding="utf-8")
    return putanja


# ----------------------------------------------------------------------
# Izbor izvora ulaznih podataka
# ----------------------------------------------------------------------
def ucitaj_iz_prodavnice(settings) -> str | None:
    """Opcioni izvor: ziva CreatorLab WooCommerce prodavnica."""
    if not settings.woocommerce_dostupan:
        print("WooCommerce kljucevi nisu postavljeni u .env - ovaj izvor je nedostupan.")
        return None
    print("Povezujem se na CreatorLab WooCommerce prodavnicu...")
    try:
        client = WooCommerceClient(settings)
        sirovi = client.fetch_products()
    except WooCommerceError as exc:
        print(f"[GRESKA - EKSTERNI PODACI] {exc}")
        return None
    proizvodi = normalizuj_proizvode(sirovi)
    if not proizvodi:
        print("Prodavnica nema objavljenih proizvoda.")
        return None
    print(f"Ucitano {len(proizvodi)} proizvoda iz prodavnice.")
    return prodavnica_kao_opis(proizvodi)


def izaberi_ulaz(settings) -> str | None:
    """Vrati pripremljen opis sistema iz izabranog izvora, ili None."""
    naslov("IZVOR ULAZNIH PODATAKA")
    print("  1) Unesi opis rucno (terminal)")
    print("  2) Ucitaj iz fajla (folder 'ulaz/')")
    print("  3) Povuci CreatorLab prodavnicu (WooCommerce)")
    izbor = unos("Izbor izvora: ")

    if izbor == "1":
        print("\nUnesi opis sistema/funkcionalnosti. Zavrsi praznim redom:")
        linije: list[str] = []
        while True:
            red = input()
            if red.strip() == "":
                break
            linije.append(red)
        tekst = "\n".join(linije)
        return pripremi_ulaz(tekst) if tekst.strip() else None

    if izbor == "2":
        fajlovi = listaj_ulazne_fajlove()
        if not fajlovi:
            print("Folder 'ulaz/' je prazan (dodaj .txt ili .md fajl).")
            return None
        print("\nDostupni fajlovi:")
        for i, f in enumerate(fajlovi, 1):
            print(f"  {i}) {f.name}")
        fi = unos("Izaberi fajl (broj): ")
        if fi.isdigit() and 1 <= int(fi) <= len(fajlovi):
            putanja = fajlovi[int(fi) - 1]
            print(f"Ucitavam: {putanja.name}")
            return ucitaj_fajl(putanja)
        print("Nevazeci izbor fajla.")
        return None

    if izbor == "3":
        return ucitaj_iz_prodavnice(settings)

    print("Nepoznat izvor.")
    return None


# ----------------------------------------------------------------------
# Rezimi rada
# ----------------------------------------------------------------------
def pokreni_rezim(agent: RizikZahteviAgent, opis: str, rezim: str) -> None:
    if rezim == "zahtevi":
        naslov("REZIM 1: Analiza zahteva")
        prefiks, naziv = "analiza_zahteva", "analizu zahteva"
        radnja = agent.analiza_zahteva
    else:
        naslov("REZIM 2: Registar rizika")
        prefiks, naziv = "registar_rizika", "procenu rizika"
        radnja = agent.registar_rizika

    print(f"\nPokrecem {naziv} (workflow od 3 koraka)...\n")
    rezultat = radnja(opis, napredak)

    print("\n" + "-" * 60)
    print(rezultat)
    print("-" * 60)

    zaglavlje = (
        f"*Model: {agent.model_naziv} | "
        f"Generisano: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"
    )
    putanja = sacuvaj_izlaz(zaglavlje + rezultat, prefiks)
    print(f"\nSacuvano u: {putanja}")


# ----------------------------------------------------------------------
# Glavni tok
# ----------------------------------------------------------------------
def main() -> None:
    naslov("AI Agent: Analiza zahteva i procena rizika (LangChain)")

    try:
        settings = load_settings()
    except ConfigError as exc:
        print(f"[GRESKA U KONFIGURACIJI] {exc}")
        sys.exit(1)

    model = izaberi_model(settings)
    try:
        agent = RizikZahteviAgent(settings, model_override=model)
    except ConfigError as exc:
        print(f"[GRESKA] {exc}")
        sys.exit(1)
    print(f"Aktivan model: {agent.model_naziv}")

    while True:
        naslov("MENI")
        print("  1) Analiza zahteva (user stories + acceptance criteria)")
        print("  2) Registar rizika (procena + mere ublazavanja)")
        print("  0) Izlaz")
        izbor = unos("Izbor: ")

        if izbor == "0":
            print("Dovidjenja!")
            break
        if izbor not in {"1", "2"}:
            print("Nepoznata opcija. Unesi 1, 2 ili 0.")
            continue

        opis = izaberi_ulaz(settings)
        if not opis:
            print("Nema validnog ulaza. Vracam se na meni.")
            continue

        try:
            pokreni_rezim(agent, opis, "zahtevi" if izbor == "1" else "rizici")
        except AgentError as exc:
            print(f"\n[GRESKA - MODEL] {exc}")


if __name__ == "__main__":
    main()
