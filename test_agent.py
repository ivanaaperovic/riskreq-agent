"""
test_agent.py
-------------
Automatska validacija agenta na vise ulaza (zahtev: test na min. 3 primera).

Propusta svaki .txt/.md fajl iz foldera 'ulaz/' kroz oba rezima agenta
(analiza zahteva + registar rizika), cuva rezultate u 'izlaz/' i ispisuje
osnovnu validaciju outputa (da li sadrzi ocekivane sekcije).

Pokretanje:  python test_agent.py
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from agent import AgentError, RizikZahteviAgent
from config import ConfigError, load_settings
from data_processing import listaj_ulazne_fajlove, ucitaj_fajl

IZLAZ_DIR = Path(__file__).parent / "izlaz"

# Ocekivane sekcije po rezimu - osnovna provera strukture izlaza.
PROVERE = {
    "analiza_zahteva": ["User stories", "Acceptance", "Nefunkcionalni"],
    "registar_rizika": ["Registar rizika", "|", "prioritet"],
}


def validiraj(tekst: str, rezim: str) -> tuple[bool, list[str]]:
    """Vrati (da_li_prolazi, lista_nedostajucih_sekcija)."""
    nedostaje = [k for k in PROVERE[rezim] if k.lower() not in tekst.lower()]
    return (not nedostaje, nedostaje)


def sacuvaj(tekst: str, naziv: str) -> Path:
    IZLAZ_DIR.mkdir(exist_ok=True)
    putanja = IZLAZ_DIR / naziv
    putanja.write_text(tekst, encoding="utf-8")
    return putanja


def main() -> None:
    try:
        settings = load_settings()
    except ConfigError as exc:
        print(f"[KONFIGURACIJA] {exc}")
        return

    agent = RizikZahteviAgent(settings)
    print(f"Model: {agent.model_naziv}")

    fajlovi = listaj_ulazne_fajlove()
    if len(fajlovi) < 3:
        print("UPOZORENJE: u 'ulaz/' ima manje od 3 fajla.")
    print(f"Testiram na {len(fajlovi)} ulaza: {[f.name for f in fajlovi]}\n")

    rezimi = [
        ("analiza_zahteva", agent.analiza_zahteva),
        ("registar_rizika", agent.registar_rizika),
    ]

    ukupno = prosli = 0
    for f in fajlovi:
        opis = ucitaj_fajl(f)
        baza = f.stem
        for rezim, radnja in rezimi:
            ukupno += 1
            print(f"[{rezim}] ulaz: {f.name} ...", end=" ", flush=True)
            try:
                rezultat = radnja(opis)
            except AgentError as exc:
                print(f"GRESKA: {exc}")
                continue

            naziv = f"TEST_{rezim}_{baza}.md"
            zaglavlje = (
                f"<!-- Test: {f.name} | rezim: {rezim} | model: {agent.model_naziv} | "
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')} -->\n\n"
            )
            putanja = sacuvaj(zaglavlje + rezultat, naziv)
            ok, nedostaje = validiraj(rezultat, rezim)
            prosli += ok
            status = "OK" if ok else f"NEPOTPUN (nedostaje: {', '.join(nedostaje)})"
            print(f"{status} -> {putanja.name}")

    print(f"\nValidacija strukture: {prosli}/{ukupno} izlaza ima sve ocekivane sekcije.")


if __name__ == "__main__":
    main()
