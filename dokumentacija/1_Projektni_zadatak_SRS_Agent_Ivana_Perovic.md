# Software Requirements Specification

## za AI agent „RiskReq" — analiza zahteva i procena rizika softverskog projekta

### Version 1.0

\

\

**Prepared by**

\

**Group Name:** Grupa III — Razvoj AI agenta (individualni rad)

| | |
|---|---|
| **Ime i prezime:** | Ivana Perović |
| **Broj indeksa:** | 1030/2022 |
| **E-mail:** | uros.mijalkovic94@gmail.com |

\

| | |
|---|---|
| **Predmet:** | Upravljanje rizikom u razvoju aplikacija elektronskog poslovanja 2025/26 |
| **Katedra:** | Katedra za elektronsko poslovanje (eLab), FON |
| **Tema:** | Grupa III — Razvoj AI agenta |
| **Datum:** | 27.06.2026. |

\pagebreak

# Sadržaj

- Revisions
- 1. Introduction (Uvod)
  - 1.1 Document Purpose
  - 1.2 Product Scope
  - 1.3 Intended Audience and Document Overview
  - 1.4 Definitions, Acronyms and Abbreviations
  - 1.5 Document Conventions
  - 1.6 References and Acknowledgments
- 2. Overall Description (Opšti opis)
  - 2.1 Product Overview
  - 2.2 Product Functionality
  - 2.3 Design and Implementation Constraints
  - 2.4 User Characteristics
  - 2.5 Assumptions and Dependencies
- 3. Specific Requirements (Specifični zahtevi)
  - 3.1 External Interface Requirements
  - 3.2 Functional Requirements
  - 3.3 Workflow agenta (Use Case Model)
- 4. Other Non-functional Requirements
  - 4.1 Performance Requirements
  - 4.2 Safety and Security Requirements
  - 4.3 Software Quality Attributes
- 5. Other Requirements
- Appendix A — Data Dictionary
- Appendix B — Individual Log

\pagebreak

# Revisions

| Version | Primary Author(s) | Description of Version | Date Completed |
|---|---|---|---|
| 1.0 | Ivana Perović | Inicijalna verzija projektnog zadatka (SRS) za AI agent „RiskReq" u okviru Grupe III. | 27.06.2026. |

\pagebreak

# 1. Introduction (Uvod)

Ovaj dokument predstavlja Specifikaciju softverskih zahteva (SRS) za **AI agent „RiskReq"** — alat koji u procesu razvoja softvera automatizuje dva zadatka koja inače obavljaju poslovni analitičar, product owner i menadžer rizika: (1) razradu zahteva u korisničke priče sa kriterijumima prihvatanja i (2) izradu registra rizika sa procenom i merama ublažavanja. Dokument je izrađen u okviru predmeta *Upravljanje rizikom u razvoju aplikacija elektronskog poslovanja* (Grupa III — Razvoj AI agenta), primenom strukture IEEE 830 standarda.

U ovoj sekciji čitalac pronalazi svrhu dokumenta, opseg proizvoda, ciljnu publiku, rečnik pojmova, konvencije i reference.

## 1.1 Document Purpose

Svrha dokumenta je da pruži jasnu, jednoznačnu i proverljivu specifikaciju funkcionalnih i nefunkcionalnih zahteva **AI agenta „RiskReq" u verziji 1.0**. SRS opisuje agenta kao softverski sistem: njegove ulazne podatke, višekoračni workflow obrade, korišćenje LLM komponente i strukturisani izlaz, kao i zahteve kvaliteta (tačnost, ponovljivost, bezbednost podataka, upotrebljivost).

Dokument služi kao osnova za implementaciju, testiranje i kritičku ocenu agenta, i kao referentni „ugovor" o tome šta agent radi i koje zahteve mora da ispuni.

## 1.2 Product Scope

**RiskReq** je AI agent (CLI aplikacija u Python-u, zasnovana na LangChain-u) koji rešava konkretan problem iz konteksta softverskog inženjerstva i upravljanja rizikom: ručna razrada zahteva i ručna izrada registra rizika su spore, nekonzistentne i zavise od iskustva pojedinca. Agent te zadatke ubrzava i standardizuje tako što iz tekstualnog opisa sistema generiše strukturisane artefakte.

**Ključne koristi:**

- Smanjuje vreme izrade prvog nacrta registra rizika i liste korisničkih priča sa nekoliko sati ručnog rada na **manje od 2 minuta** po ulazu.
- Standardizuje format izlaza (uvek iste sekcije, ista skala procene rizika), čime se smanjuje varijabilnost među analitičarima.
- Služi kao „prvi nacrt" koji čovek (PO / menadžer rizika) zatim kritički proverava i dopunjava — ne zamenjuje stručnjaka, već ubrzava njegov rad.

**Strateški cilj u kontekstu predmeta:** demonstrirati kako se AI alat (LLM + LangChain) može odgovorno koristiti u procesu razvoja, uz fokus na **identifikaciju, analizu i upravljanje rizicima** softverskog proizvoda.

## 1.3 Intended Audience and Document Overview

- **Project manager / Product owner** — koristi izlaze agenta kao polaznu osnovu za backlog i plan upravljanja rizicima.
- **Poslovni analitičar / QA inženjer** — koristi generisane priče i kriterijume prihvatanja.
- **Predmetni nastavnik i komisija** — za ocenu obuhvata i kvaliteta rešenja.
- **Budući korisnik/developer agenta** — kao osnova za pokretanje, izmenu i proširenje.

**Preporučeni redosled čitanja:** Sekcija 1 (kontekst) → Sekcija 2 (opšti opis i workflow) → Sekcija 3 (funkcionalni zahtevi) → Sekcija 4 (nefunkcionalni zahtevi) → Dodaci.

## 1.4 Definitions, Acronyms and Abbreviations

| Skraćenica | Značenje |
|---|---|
| AI | Artificial Intelligence (veštačka inteligencija) |
| API | Application Programming Interface |
| BA | Business Analyst (poslovni analitičar) |
| CLI | Command-Line Interface |
| FR | Functional Requirement (funkcionalni zahtev) |
| LLM | Large Language Model (veliki jezički model) |
| NFR | Non-Functional Requirement (nefunkcionalni zahtev) |
| PO | Product Owner |
| PM | Project Manager |
| REST | Representational State Transfer |
| RPN / Nivo rizika | Risk Priority Number = Verovatnoća × Uticaj |
| SRS | Software Requirements Specification |
| US | User Story (korisnička priča) |
| WC | WooCommerce |

## 1.5 Document Conventions

- **ID konvencija:** funkcionalni zahtevi `REQ-F-NNN`, nefunkcionalni `REQ-NF-NNN`, koraci workflow-a `A1–A3` (analiza zahteva) i `B1–B3` (registar rizika).
- **Formulacija:** „mora" (shall) za obavezne, „trebalo bi" (should) za poželjne zahteve. Nemerljivi termini (*brzo*, *pouzdano*) zamenjeni proverljivim formulacijama (npr. „≤ 2 min", „skala 1–5").
- **Format funkcionalnog zahteva:** Naziv, Opis, Prioritet, Izvor, Kriterijum prihvatanja.

## 1.6 References and Acknowledgments

- **IEEE 830-1998** — *Recommended Practice for Software Requirements Specifications*.
- **ISO/IEC/IEEE 29148:2018** — *Requirements engineering*.
- **ISO 31000:2018** — *Risk management — Guidelines*.
- **LangChain dokumentacija** — https://python.langchain.com/
- **Teme za seminarske radove — URIZ 2026**, Katedra za e-poslovanje (eLab), FON, 2026.
- Tehnička osnova agenta preuzeta i prilagođena iz autorovog ranijeg LangChain projekta (CreatorLab AI Agent).

**Acknowledgments:** Veliki jezički model (Ollama `llama3.2` lokalno; arhitektura podržava i OpenAI) korišćen je kao izvršna LLM komponenta agenta. AI asistencija korišćena je i u procesu formulacije dokumentacije.

\pagebreak

# 2. Overall Description (Opšti opis)

## 2.1 Product Overview

**RiskReq** je samostalan AI agent realizovan kao **CLI aplikacija**. Nije chatbot: za jedan ulaz izvršava **fiksiran višekoračni workflow** (3 koraka po režimu) u kome izlaz jednog koraka postaje ulaz sledećeg, i vraća strukturisani Markdown izveštaj koji se i prikazuje i čuva u fajl.

Agent ima **dva režima rada**:

1. **Analiza zahteva** — iz opisa sistema generiše aktere, funkcionalne celine, korisničke priče i kriterijume prihvatanja + kvantifikovane nefunkcionalne zahteve.
2. **Registar rizika** — iz opisa sistema identifikuje komponente i rizike, procenjuje ih (Verovatnoća × Uticaj) i predlaže mere ublažavanja.

**Dijagram visokog nivoa:**

```
        [ Korisnik (PM / PO / analitičar) — terminal ]
                          │  opis sistema / izbor režima
                          ▼
        ┌─────────────────────────────────────────┐
        │                 RiskReq                  │
        │  ┌────────────────────────────────────┐ │
        │  │ Ulaz: terminal / fajl / WooCommerce│ │  ◄── (opciono) CreatorLab
        │  └──────────────┬─────────────────────┘ │       WooCommerce API
        │  ┌──────────────▼─────────────────────┐ │
        │  │ data_processing: čišćenje, chunking│ │
        │  └──────────────┬─────────────────────┘ │
        │  ┌──────────────▼─────────────────────┐ │
        │  │ agent: workflow od 3 LLM koraka    │ │
        │  │ prompts.py  +  llm_provider.py     │─┼──► LLM (Ollama / OpenAI)
        │  └──────────────┬─────────────────────┘ │
        │  ┌──────────────▼─────────────────────┐ │
        │  │ strukturisan Markdown izlaz        │ │
        │  └────────────────────────────────────┘ │
        └─────────────────────────────────────────┘
                          │
                          ▼
                  terminal + izlaz/*.md
```

## 2.2 Product Functionality

- **Učitavanje ulaza** iz tri izvora: direktan unos, tekstualni fajl (`ulaz/`), i opciono živa CreatorLab WooCommerce prodavnica (e-commerce aplikacija kao predmet analize).
- **Obrada ulaza** pre LLM-a: čišćenje HTML-a/praznina, skraćivanje (chunking) predugog teksta.
- **Režim 1 — Analiza zahteva** (workflow A1→A2→A3).
- **Režim 2 — Registar rizika** (workflow B1→B2→B3).
- **Izbor LLM modela/provajdera** (Ollama lokalno ili OpenAI) preko `.env` i menija.
- **Strukturisan izlaz** u Markdown-u + čuvanje u `izlaz/`.
- **Obrada grešaka** (nedostupan model, pogrešan ključ, timeout, limit, nedostupna prodavnica).

## 2.3 Design and Implementation Constraints

- **Jezik/okvir:** Python 3.10+; **LangChain** za orkestraciju LLM lanaca.
- **LLM:** lokalni **Ollama** (`llama3.2`) podrazumevano; alternativno **OpenAI** (`gpt-4o-mini` i dr.) — zamena jednom promenljivom u `.env`.
- **Modularnost:** odvojeni moduli `config`, `data_processing`, `llm_provider`, `prompts`, `agent`, `main`.
- **Tajne:** API ključevi isključivo u `.env` (u `.gitignore`), nikad hardkodovani.
- **Interfejs:** CLI (terminal); bez grafičkog interfejsa u v1.

## 2.4 User Characteristics

| Uloga | Potrebe |
|---|---|
| **Project manager** | Brz pregled rizika projekta sa prioritetima i merama; polazna osnova za plan upravljanja rizicima. |
| **Product owner** | Razrada ideje u korisničke priče sa jasnim kriterijumima prihvatanja za backlog. |
| **Poslovni analitičar / QA** | Konzistentan format zahteva i kriterijuma; ušteda na ručnoj razradi. |
| **Menadžer rizika** | Standardizovan registar rizika sa numeričkom procenom (V×U). |

## 2.5 Assumptions and Dependencies

- Pretpostavlja se da je na mašini pokrenut Ollama servis sa skinutim modelom (`ollama pull llama3.2`) **ili** da postoji važeći `OPENAI_API_KEY`.
- Pretpostavlja se da je ulazni opis na srpskom/engleskom i da je dovoljno informativan (bar nekoliko rečenica).
- Za izvor „WooCommerce" pretpostavlja se da je CreatorLab prodavnica pokrenuta i dostupna (REST API ključevi u `.env`).
- Kvalitet izlaza zavisi od kvaliteta LLM modela; lokalni manji model daje slabije rezultate od većih komercijalnih modela (vidi sekciju 4 i kritičku ocenu).

\pagebreak

# 3. Specific Requirements (Specifični zahtevi)

## 3.1 External Interface Requirements

### 3.1.1 User Interfaces
CLI (terminal): meni za izbor modela, režima i izvora ulaza; ispis napretka po koracima; prikaz strukturisanog rezultata.

### 3.1.2 Software Interfaces
- **LLM provajder:** Ollama (lokalni HTTP API, `http://localhost:11434`) ili OpenAI (REST API, autorizacija API ključem).
- **WooCommerce REST API** (opciono) — OAuth 1.0a, čitanje proizvoda.
- **Fajl sistem:** čitanje iz `ulaz/`, upis u `izlaz/`.

### 3.1.3 Communications Interfaces
HTTPS/HTTP ka LLM i WooCommerce API-ju; lokalna komunikacija ka Ollama serveru.

## 3.2 Functional Requirements

### F1. Učitavanje i obrada ulaza

**REQ-F-001 — Izbor izvora ulaza**
*Opis:* Sistem mora omogućiti korisniku izbor izvora ulaznih podataka: (a) direktan unos, (b) fajl iz `ulaz/`, (c) WooCommerce prodavnica.
*Prioritet:* Visok
*Izvor:* Zahtev #6 (jasno definisani ulazni podaci).
*Kriterijum prihvatanja:* Za svaki od tri izvora sistem vraća pripremljen tekstualni opis ili jasnu poruku ako izvor nije dostupan.

**REQ-F-002 — Priprema ulaza**
*Opis:* Pre slanja modelu, sistem mora očistiti ulaz (HTML, višak praznina) i skratiti tekst duži od limita (chunking).
*Prioritet:* Srednji
*Izvor:* Optimizacija troška tokena i kvaliteta.
*Kriterijum prihvatanja:* Tekst duži od 4000 karaktera se skraćuje na granici rečenice uz oznaku skraćivanja.

### F2. Režim 1 — Analiza zahteva

**REQ-F-003 — Izdvajanje aktera i funkcionalnih celina (korak A1)**
*Opis:* Iz opisa sistema agent mora izdvojiti aktere i glavne funkcionalne celine.
*Prioritet:* Visok
*Izvor:* Zahtev #8 (višekoračni workflow).
*Kriterijum prihvatanja:* Izlaz sadrži sekcije „Akteri" i „Funkcionalne celine".

**REQ-F-004 — Generisanje korisničkih priča (korak A2)**
*Opis:* Na osnovu A1, agent mora generisati user stories u formatu „Kao <uloga>, želim <cilj>, kako bih <vrednost>" sa jedinstvenim ID-jem.
*Prioritet:* Visok
*Izvor:* Zahtev #7 (strukturisan izlaz).
*Kriterijum prihvatanja:* Svaka priča ima ID (US-n) i sva tri elementa formata.

**REQ-F-005 — Kriterijumi prihvatanja i nefunkcionalni zahtevi (korak A3)**
*Opis:* Na osnovu A2, agent mora dodati acceptance criteria i listu kvantifikovanih nefunkcionalnih zahteva.
*Prioritet:* Visok
*Izvor:* Zahtevi #5, #8.
*Kriterijum prihvatanja:* Izlaz sadrži sekcije „User stories sa acceptance criteria" i „Nefunkcionalni zahtevi" (tabela sa merljivim metama).

### F3. Režim 2 — Registar rizika

**REQ-F-006 — Izdvajanje komponenti (korak B1)**
*Opis:* Iz opisa sistema agent mora izdvojiti ključne komponente i resurse relevantne za rizik.
*Prioritet:* Visok
*Izvor:* Zahtev #8.
*Kriterijum prihvatanja:* Izlaz sadrži numerisanu listu komponenti sa obrazloženjem.

**REQ-F-007 — Identifikacija rizika (korak B2)**
*Opis:* Za svaku komponentu agent mora identifikovati konkretne rizike sa kategorijom.
*Prioritet:* Visok
*Izvor:* Cilj predmeta (identifikacija rizika).
*Kriterijum prihvatanja:* Svaki rizik ima ID (R-n), opis, komponentu i kategoriju.

**REQ-F-008 — Procena i registar rizika (korak B3)**
*Opis:* Agent mora proceniti svaki rizik (Verovatnoća 1–5, Uticaj 1–5, Nivo = V×U), oceniti ga (Nizak/Srednji/Visok), predložiti strategiju i meru ublažavanja, i sve prikazati u tabeli „Registar rizika" + listi Top 3 prioriteta.
*Prioritet:* Visok
*Izvor:* Zahtev #7; ISO 31000.
*Kriterijum prihvatanja:* Izlaz sadrži tabelu registra sa svim kolonama i sekciju „Top 3 prioritetna rizika".

### F4. LLM, izlaz i robusnost

**REQ-F-009 — Izbor LLM modela/provajdera**
*Opis:* Sistem mora omogućiti izbor provajdera (Ollama/OpenAI) i modela (preko `.env` i menija).
*Prioritet:* Srednji
*Izvor:* Zahtev #10 (LLM komponenta), obavezni alati.
*Kriterijum prihvatanja:* Promenom `LLM_PROVIDER` u `.env` menja se izvršni model bez izmene koda.

**REQ-F-010 — Čuvanje strukturisanog izlaza**
*Opis:* Sistem mora sačuvati rezultat kao Markdown fajl u `izlaz/` sa vremenskom oznakom i metapodacima (model, datum).
*Prioritet:* Srednji
*Izvor:* Zahtev #7.
*Kriterijum prihvatanja:* Po izvršenju režima nastaje `.md` fajl čiji sadržaj odgovara prikazanom u terminalu.

**REQ-F-011 — Obrada grešaka**
*Opis:* Greške (pogrešan ključ, timeout, limit zahteva, nedostupan model/prodavnica) sistem mora uhvatiti i prikazati jasnu poruku, bez pada aplikacije.
*Prioritet:* Visok
*Izvor:* Nefunkcionalni zahtev pouzdanosti.
*Kriterijum prihvatanja:* Pri izazvanoj grešci aplikacija ispisuje razumljivu poruku i vraća se u meni.

## 3.3 Workflow agenta (Use Case Model)

### Akteri
- **Korisnik (PM / PO / analitičar / menadžer rizika)** — pokreće agenta, bira režim i izvor, koristi izlaz.

### Use Case U1 — Generisanje registra rizika

- **Purpose:** Iz opisa sistema dobiti procenjen registar rizika sa merama.
- **Requirements Traceability:** REQ-F-001, REQ-F-006, REQ-F-007, REQ-F-008, REQ-F-010.
- **Preconditions:** Pokrenut LLM (Ollama/OpenAI); dostupan opis sistema.
- **Postconditions:** Registar rizika prikazan i sačuvan u `izlaz/`.
- **Basic Flow:**
  1. Korisnik bira režim „Registar rizika".
  2. Bira izvor ulaza i unosi/učitava opis sistema.
  3. Agent izvršava korak B1 (komponente).
  4. Agent izvršava korak B2 (rizici po komponenti).
  5. Agent izvršava korak B3 (procena V×U + mere) i sastavlja registar.
  6. Sistem prikazuje i čuva strukturisan izveštaj.
- **Exceptions:** LLM nedostupan/timeout → jasna poruka, povratak u meni; prazan ulaz → odbijanje sa porukom.

### Use Case U2 — Analiza zahteva

- **Purpose:** Iz opisa sistema dobiti user stories sa acceptance criteria i NFR.
- **Requirements Traceability:** REQ-F-001, REQ-F-003, REQ-F-004, REQ-F-005, REQ-F-010.
- **Basic Flow:** izbor režima → ulaz → A1 (akteri/celine) → A2 (user stories) → A3 (kriterijumi + NFR) → prikaz i čuvanje.

\pagebreak

# 4. Other Non-functional Requirements

## 4.1 Performance Requirements

**REQ-NF-001 — Vreme obrade**
Agent mora kompletirati workflow od 3 koraka u **≤ 2 min po ulazu** pri lokalnom Ollama `llama3.2` modelu na prosečnom laptopu, odnosno **≤ 30 s** pri OpenAI `gpt-4o-mini`.

**REQ-NF-002 — Veličina ulaza**
Agent mora obraditi ulaz do **4000 karaktera** bez greške; duži ulaz se automatski skraćuje (REQ-F-002).

## 4.2 Safety and Security Requirements

**REQ-NF-003 — Zaštita tajni**
API ključevi i WooCommerce kredencijali moraju biti isključivo u `.env` (u `.gitignore`); ne smeju se logovati niti commit-ovati.

**REQ-NF-004 — Privatnost ulaza**
Pri korišćenju OpenAI provajdera, ulazni podaci se šalju eksternom servisu; za poverljive podatke mora postojati mogućnost potpuno lokalne obrade (Ollama) — agent to podržava bez izmene koda.

## 4.3 Software Quality Attributes

**REQ-NF-005 — Tačnost / korisnost (kvantifikovano)**
Na test skupu od najmanje 3 ulaza, ≥ **80%** generisanih stavki (priča / rizika) mora biti relevantno i primenljivo prema oceni korisnika (validacija u sekciji testiranja).

**REQ-NF-006 — Ponovljivost**
Pri `LLM_TEMPERATURE=0` izlaz za isti ulaz mora biti stabilan po strukturi (iste sekcije) i suštinski konzistentan.

**REQ-NF-007 — Strukturisanost izlaza**
≥ **90%** pokretanja mora dati izlaz sa svim propisanim sekcijama (automatska provera u `test_agent.py`).

**REQ-NF-008 — Razumljivost**
Izlaz mora biti na srpskom jeziku, u Markdown formatu sa jasno označenim sekcijama.

**REQ-NF-009 — Održivost / modularnost**
Dodavanje novog režima mora biti moguće dodavanjem prompta u `prompts.py` i metode u `agent.py`, bez izmene `main` toka više od jedne grane menija.

**REQ-NF-010 — Prenosivost**
Aplikacija mora raditi na Windows/macOS/Linux uz Python 3.10+ i instalirane zavisnosti iz `requirements.txt`.

\pagebreak

# 5. Other Requirements

- **Dokumentacija:** projekat mora sadržati `README.md` sa koracima instalacije i pokretanja, i kritičku ocenu (ograničenja, rizici, unapređenja).
- **Reproducibilnost testa:** `test_agent.py` mora propustiti sve ulaze iz `ulaz/` kroz oba režima i izvestiti o pokrivenosti sekcija.

\pagebreak

# Appendix A — Data Dictionary

## A.1 Glavne strukture podataka

| Struktura | Polja | Opis |
|---|---|---|
| `Settings` | llm_provider, openai_*, ollama_*, wc_*, request_timeout, llm_temperature | Učitana konfiguracija iz `.env`. |
| `Proizvod` | id, naziv, cena, opis, kategorije | Normalizovan proizvod iz WooCommerce izvora. |
| Ulaz (opis) | string (≤ 4000 char) | Pripremljen tekstualni opis sistema. |
| Izlaz (izveštaj) | Markdown string | Strukturisan rezultat (3 sekcije po koraku). |

## A.2 Skala procene rizika

| Dimenzija | Vrednosti | Značenje |
|---|---|---|
| Verovatnoća (V) | 1–5 | 1 = vrlo niska … 5 = vrlo visoka |
| Uticaj (U) | 1–5 | 1 = zanemarljiv … 5 = kritičan |
| Nivo (V×U) | 1–25 | 1–6 Nizak, 8–12 Srednji, 15–25 Visok |
| Strategija | izbegavanje / ublažavanje / prenos / prihvatanje | Standardne strategije (ISO 31000) |

## A.3 Konfiguracione konstante

| Naziv | Podrazumevano | Opis |
|---|---|---|
| `MAX_ULAZ_LEN` | 4000 | Maks. dužina ulaza poslata modelu. |
| `MAX_OPIS_LEN` | 600 | Maks. dužina opisa po proizvodu (WC izvor). |
| `REQUEST_TIMEOUT` | 120 | Tajmaut poziva (s). |
| `LLM_TEMPERATURE` | 0.3 | Temperatura modela. |

\pagebreak

# Appendix B — Individual Log

| Datum | Aktivnost | Napomena |
|---|---|---|
| 27.06.2026. | Izbor teme (Grupa III) i analiza zahteva | Pregled URIZ tema; reuse postojećeg LangChain agenta. |
| 27.06.2026. | Preusmeravanje namene agenta (marketing → analiza zahteva/rizika) | Zadržana arhitektura, promenjen use-case i promptovi. |
| 27.06.2026. | Implementacija višekoračnog workflow-a (A1–A3, B1–B3) | `prompts.py`, `agent.py`, `main.py`. |
| 27.06.2026. | Testiranje na 3 ulaza + validacija | `test_agent.py`, rezultati u `izlaz/`. |
| 27.06.2026. | Pisanje projektnog zadatka (SRS) i dokumentacije | Ovaj dokument + README + kritička ocena. |

**Korišćeni AI alati:** LLM komponenta agenta (Ollama `llama3.2` / OpenAI), AI asistencija u izradi dokumentacije.
