# Seminarski rad

## Razvoj AI agenta „RiskReq" - analiza zahteva i procena rizika softverskog projekta

**Predmet:** Upravljanje rizikom u razvoju aplikacija elektronskog poslovanja 2025/26
**Katedra:** Katedra za elektronsko poslovanje (eLab), FON
**Tema:** Grupa III - Razvoj AI agenta (individualni rad)

| | |
|---|---|
| **Ime i prezime:** | Ivana Perović |
| **Broj indeksa:** | 1030/2022 |
| **GitHub repozitorijum:** | https://github.com/ivanaaperovic/riskreq-agent |
| **JIRA projekat:** | RISKREQ (ivanaperovic.atlassian.net) |
| **Datum:** | 07.07.2026. |

\pagebreak

# Sadržaj

- Deo 1. Projektni zadatak (SRS)
- Deo 2. JIRA projekat (epike, priče, taskovi, board)
- Deo 3. Povezivanje JIRA i GitHub
- Deo 4. Testiranje i validacija
- Deo 5. Kritička ocena
- Prilog A. Screenshot dokazi (JIRA i GitHub)

> Napomena o strukturi: ceo tekst projektnog zadatka (SRS) dat je u zasebnom fajlu
> `1_Projektni_zadatak_SRS_Agent_Ivana_Perovic.md` i sažet je u Delu 1. Delovi 2-5
> objedinjuju JIRA, GitHub, testiranje i kritičku ocenu, sa priloženim dokazima u Prilogu A.

\pagebreak

# Deo 1. Projektni zadatak (SRS) - sažetak

Pun projektni zadatak izrađen je po strukturi IEEE 830 standarda (fajl
`1_Projektni_zadatak_SRS_Agent_Ivana_Perovic.md`). Ovde je dat sažetak ključnih tačaka.

**Šta je RiskReq.** Samostalan AI agent (CLI aplikacija u Python-u, LangChain), nije chatbot.
Za jedan ulaz izvršava fiksiran višekoračni workflow (3 koraka po režimu) u kome izlaz
jednog koraka postaje ulaz sledećeg, i vraća strukturisani Markdown izveštaj.

**Dva režima rada:**

1. **Analiza zahteva** (workflow A1 -> A2 -> A3): iz opisa sistema generiše aktere,
   funkcionalne celine, korisničke priče i kriterijume prihvatanja + kvantifikovane NFR.
2. **Registar rizika** (workflow B1 -> B2 -> B3): iz opisa sistema identifikuje komponente
   i rizike, procenjuje ih (Verovatnoća x Uticaj) i predlaže mere ublažavanja.

**Ulaz** iz tri izvora: direktan unos, tekstualni fajl (`ulaz/`), i opciono živa CreatorLab
WooCommerce prodavnica. **Izlaz** strukturisan Markdown, sačuvan u `izlaz/`.

**Ispunjenje obaveznih elemenata Grupe III:**

| Zahtev Grupe III | Kako je ispunjeno |
|---|---|
| Jasno definisani ulazni podaci | 3 izvora ulaza (terminal / fajl / WooCommerce) |
| Workflow od 2-3 koraka | 3 koraka po režimu (A1-A3, B1-B3), ulančavanje LangChain |
| LLM komponenta | Ollama `llama3.2` lokalno ili OpenAI (`.env`) |
| Strukturisan izlaz | Markdown sa fiksnim sekcijama, čuvanje u `izlaz/` |
| Test na min. 3 ulaza | 3 ulaza x 2 režima = 6 pokretanja (Deo 4) |
| Dokumentacija + kritička ocena | Ovaj dokument, README, Deo 5 |
| JIRA projekat | Deo 2 |
| JIRA <-> GitHub veza | Deo 3 |

**Ključni funkcionalni zahtevi:** REQ-F-001..011 (izbor izvora, priprema ulaza, koraci
A1-A3 i B1-B3, izbor LLM provajdera, čuvanje izlaza, obrada grešaka).

**Ključni nefunkcionalni zahtevi:** vreme obrade <= 2 min (Ollama) / <= 30 s (OpenAI),
ulaz do 4000 karaktera, zaštita tajni (`.env` u `.gitignore`), ponovljivost pri
`temperature=0`, >= 90% pokretanja sa svim sekcijama.

\pagebreak

# Deo 2. JIRA projekat

Rad na razvoju agenta organizovan je u JIRA-i kroz strukturu **epike -> korisničke priče ->
taskovi -> subtaskovi**, sa statusima i prioritetima.

- **Projekat (key):** `RISKREQ` („RiskReq Agent")
- **Instanca:** ivanaperovic.atlassian.net
- **Tip:** team-managed Scrum (Backlog + Sprint board: To Do / In Progress / Done)
- **Assignee:** Ivana Perović (individualni rad)
- **Obim:** 40 stavki = 6 Epic + 10 Task (korisničke priče) + 24 Subtask; aktivan Sprint 1

## Pregled epika

| Epic | Naziv | Status |
|---|---|---|
| EPIC-1 | Postavka projekta i infrastruktura | Done |
| EPIC-2 | Učitavanje i obrada ulaza | Done |
| EPIC-3 | Režim „Analiza zahteva" (workflow A) | Done |
| EPIC-4 | Režim „Registar rizika" (workflow B) | Done |
| EPIC-5 | Testiranje i validacija | Done |
| EPIC-6 | Dokumentacija | Done |

## Korisničke priče (izbor)

- **US-5:** Kao PO, želim user stories iz opisa sistema, kako bih popunio backlog.
- **US-6:** Kao menadžer rizika, želim registar rizika sa procenom (V x U) i merama.
- **US-8:** Kao developer, želim test na >= 3 ulaza, kako bih potvrdio da agent radi i da je
  izlaz strukturisan.
- **US-10:** Kao komisija, želim projektni zadatak (SRS), kako bih ocenila obuhvat.

Svaka priča je razložena na taskove i subtaskove (npr. TASK-5.1 Prompt A1, TASK-5.2 Prompt A2,
TASK-5.3 Prompt A3, TASK-5.4 ulančavanje 3 koraka).

## Dokaz: Scrum board (zahtev #12)

Kolone To Do / In Progress / Done sa raspoređenim stavkama Sprint-a 1.

![JIRA Scrum board sa kolonama To Do / In Progress / Done](slike/sc3_board.png)

## Dokaz: Backlog (zahtev #12)

Backlog sa epikama i korisničkim pričama.

![JIRA Backlog sa epikama i pričama](slike/sc4_backlog.png)

\pagebreak

# Deo 3. Povezivanje JIRA i GitHub (zahtev #13)

Cilj: prikazati kako se JIRA zadaci (npr. `RISKREQ-13`) povezuju sa GitHub aktivnostima -
granama, commit-ovima i Pull Request-ovima.

## Konvencija: ključ issue-a u svemu

- **Grana po zadatku:** `git checkout -b RISKREQ-13-jira-github`
- **Commit poruka sadrži ključ:** `git commit -m "RISKREQ-6 Workflow B (komponente, rizici, V x U)"`
- **PR naslov sadrži ključ:** `RISKREQ-13 Povezivanje JIRA i GitHub`

Zahvaljujući tome, JIRA na kartici issue-a automatski prikazuje granu, commit-ove i PR
(sekcija *Development*).

## Realizovana veza

- Instaliran je zvanični **„GitHub for Jira"** app i povezan repozitorijum
  `ivanaaperovic/riskreq-agent` (javan).
- Napravljeno je 6 commit-ova sa `RISKREQ-*` ključevima; otvoren i **merdžovan Pull Request #1**
  (grana `RISKREQ-13-jira-github` -> `main`).
- Projektni **Development** tab u JIRA-i prikazuje povezani repo i završene work item-e.

## Primer mapiranja JIRA <-> GitHub

| JIRA issue | GitHub grana | PR |
|---|---|---|
| RISKREQ-5 (analiza zahteva) | `RISKREQ-5-analiza-zahteva` | RISKREQ-5 Analiza zahteva |
| RISKREQ-6 (registar rizika) | `RISKREQ-6-registar-rizika` | RISKREQ-6 Registar rizika |
| RISKREQ-13 (JIRA-GitHub) | `RISKREQ-13-jira-github` | RISKREQ-13 Povezivanje (PR #1, merged) |

## Dokaz: Development / Related work

Projekat -> Development -> Related work: pod-kartice Pull requests (vidi PR #1) i Repositories
(vidi povezani repo).

![JIRA Development - Related work (Pull requests + Repositories)](slike/sc1_related_work.png)

## Dokaz: kartica RISKREQ-13 sa Development sekcijom (glavni dokaz)

Kartica issue-a RISKREQ-13, desno sekcija *Development* sa granom, commit-om i PR-om.

![JIRA kartica RISKREQ-13 - Development sekcija](slike/sc2_riskreq13.png)

## Dokaz: GitHub Pull Request #1

Merdžovan PR #1 na GitHub-u.

![GitHub Pull Request #1 (merged)](slike/sc5_pr.png)

\pagebreak

# Deo 4. Testiranje i validacija (zahtev #14)

Agent je testiran na **3 ulaza** (CreatorLab e-commerce, SkillSwap platforma, MobaBank
mobilno bankarstvo), svaki kroz **oba režima** = 6 pokretanja, sa lokalnim modelom
`llama3.2`. Svih 6 izlaza prošlo je automatsku **validaciju strukture** (`test_agent.py`):
sadrže sve propisane sekcije. Rezultati su u `izlaz/TEST_*.md`.

**Validacija sadržaja (ručna ocena):**

| Aspekt | Ocena | Komentar |
|---|---|---|
| Struktura izlaza | vrlo dobra | Sve sekcije prisutne, workflow vidljiv kroz 3 koraka. |
| Relevantnost stavki | dobra | Akteri, celine i rizici odgovaraju ulazu (npr. za banku: autentikacija, regulativa, core banking). |
| Procena rizika (V x U) | smislena | Najviši nivoi dodeljeni bezbednosnim rizicima. |
| Jezička ispravnost | osrednja | `llama3.2` povremeno klizi u rogobatne forme. |
| Doslednost tabele | povremeni propusti | Mali model ponekad izostavi ćeliju u redu tabele. |

\pagebreak

# Deo 5. Kritička ocena (zahtev #15)

## Korišćene tehnologije i biblioteke

| Sloj | Tehnologija |
|---|---|
| Jezik | Python 3.10+ |
| Orkestracija LLM-a | LangChain (`langchain-core`, `ChatPromptTemplate`, `StrOutputParser`) |
| LLM provajder | Ollama (`llama3.2`, lokalno) i/ili OpenAI (`gpt-4o-mini`) |
| Konfiguracija | `python-dotenv` (`.env`) |
| Opcioni izvor podataka | WooCommerce REST API (`woocommerce`, `requests`) |

Instalacija i pokretanje detaljno u `README.md` (venv -> `pip install -r requirements.txt`
-> `.env` -> `python main.py`). Test: `python test_agent.py`.

## Ograničenja

1. **Kvalitet zavisi od modela.** Lokalni `llama3.2` daje rogobatan jezik i povremene
   formatne propuste; `gpt-4o-mini`/`gpt-4o` znatno bolji (uz trošak i eksterno slanje).
2. **Nema garancije tačnosti (halucinacije).** Izlaz je prvi nacrt, ne konačan dokument.
3. **Plitka procena rizika.** V i U su procena LLM-a, bez kvantitativnih podataka. Ne
   zamenjuje formalnu FMEA.
4. **Ulaz ograničen na ~4000 karaktera** (chunking).
5. **CLI, bez perzistencije.** Svaki poziv je nezavisan.
6. **Nedeterminizam** pri `temperature > 0`.

## Rizici korišćenja agenta

| Rizik | Mera ublažavanja |
|---|---|
| Preterano poverenje u AI | Označiti izlaz kao „nacrt za reviziju"; obavezna ljudska provera. |
| Curenje poverljivih podataka | Koristiti lokalni Ollama za poverljive ulaze. |
| Lažan osećaj potpunosti | Tretirati kao polaznu listu; dopuniti domenskim znanjem. |
| Nekonzistentnost | Postaviti `LLM_TEMPERATURE=0` za ponovljivost. |

## Mogućnosti za unapređenje

- Strukturisani izlaz preko sheme (Pydantic / `with_structured_output`) protiv formatnih propusta.
- RAG nad standardima (ISO 31000, OWASP) za utemeljene rizike.
- Direktan export registra u CSV/JIRA (zatvoriti petlju ka JIRA).
- Veb interfejs (Streamlit) umesto CLI.
- Evaluacioni sloj (LLM-as-judge).
- Podrazumevano jači model za srpski jezik uz lokalni fallback.

## Zaključak

Agent ispunjava cilj Grupe III: rešava konkretan problem iz domena softverskog inženjerstva
i upravljanja rizikom, ima jasno definisan ulaz, višekoračni workflow (3 koraka), LLM
komponentu i strukturisan izlaz, i nije običan chatbot. Prava vrednost je u ubrzavanju
prvog nacrta analize zahteva i registra rizika - uz obaveznu ljudsku reviziju. Glavno
ograničenje je kvalitet jezika lokalnog modela, što se rešava prelaskom na jači model
jednom linijom u `.env`.

\pagebreak

# Prilog A. Screenshot dokazi

Svi dokazi povezivanja i JIRA organizacije nalaze se u folderu `slike/`:

| Fajl | Šta prikazuje | Zahtev |
|---|---|---|
| `sc1_related_work.png` | JIRA Development -> Related work (PR + Repositories) | #13 |
| `sc2_riskreq13.png` | Kartica RISKREQ-13, Development sekcija | #13 |
| `sc3_board.png` | Scrum board (To Do / In Progress / Done) | #12 |
| `sc4_backlog.png` | Backlog (epike + priče) | #12 |
| `sc5_pr.png` | GitHub Pull Request #1 (merged) | #13 |

**Link ka repozitorijumu:** https://github.com/ivanaaperovic/riskreq-agent
