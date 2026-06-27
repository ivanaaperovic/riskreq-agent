# JIRA projekat — razvoj AI agenta „RiskReq"

Ovaj dokument definiše JIRA projekat za organizaciju rada na razvoju agenta:
**epike → user stories → taskove → subtaskove**, sa statusima, prioritetima i zaduženjima.
Uz dokument ide i `3_JIRA_import.csv` za uvoz u JIRA (*Settings → System → External System Import → CSV*).

- **Projekat ( key):** `RISKREQ`
- **Tip:** Scrum (Backlog + Sprint board: To Do / In Progress / Review / Done)
- **Zaduženja (Assignee):** Ivana Perović (individualni rad)

---

## Pregled epika

| Epic ID | Naziv | Cilj | Status |
|---|---|---|---|
| EPIC-1 | Postavka projekta i infrastruktura | venv, zavisnosti, `.env`, izbor LLM provajdera | Done |
| EPIC-2 | Učitavanje i obrada ulaza | tri izvora ulaza + priprema teksta | Done |
| EPIC-3 | Režim „Analiza zahteva" (workflow A) | A1→A2→A3 | Done |
| EPIC-4 | Režim „Registar rizika" (workflow B) | B1→B2→B3 | Done |
| EPIC-5 | Testiranje i validacija | test na ≥3 ulaza, provera strukture | Done |
| EPIC-6 | Dokumentacija | SRS, README, kritička ocena, JIRA/GitHub | In Progress |

---

## EPIC-1 — Postavka projekta i infrastruktura  *(Prioritet: High)*

- **US-1:** Kao developer, želim modularnu strukturu projekta, kako bih lako proširivao agenta.
  - TASK-1.1 Kreirati module `config/llm_provider/data_processing/prompts/agent/main` — *Done*
  - TASK-1.2 `requirements.txt` + `venv` — *Done*
- **US-2:** Kao developer, želim da biram LLM provajdera/model, kako bih radio lokalno (Ollama) ili preko OpenAI.
  - TASK-2.1 Fabrika `llm_provider.kreiraj_llm` (Ollama + OpenAI) — *Done*
  - TASK-2.2 `.env` + validacija ključeva (`config.py`) — *Done*
  - SUBTASK-2.2.1 Učiniti WooCommerce ključeve opcionim — *Done*

## EPIC-2 — Učitavanje i obrada ulaza  *(Prioritet: High)*

- **US-3:** Kao korisnik, želim da unesem opis sistema na 3 načina (terminal/fajl/prodavnica).
  - TASK-3.1 Direktan unos sa terminala — *Done*
  - TASK-3.2 Učitavanje iz `ulaz/*.txt` — *Done*
  - TASK-3.3 Opcioni WooCommerce izvor (`prodavnica_kao_opis`) — *Done*
- **US-4:** Kao developer, želim pripremu ulaza (čišćenje + chunking), kako bih kontrolisao trošak tokena.
  - TASK-4.1 `ocisti_html` / `pripremi_ulaz` / `skrati` — *Done*

## EPIC-3 — Režim „Analiza zahteva" (workflow A)  *(Prioritet: High)*

- **US-5:** Kao PO, želim user stories iz opisa sistema, kako bih popunio backlog.
  - TASK-5.1 Prompt A1 (akteri + celine) — *Done*
  - TASK-5.2 Prompt A2 (user stories) — *Done*
  - TASK-5.3 Prompt A3 (acceptance criteria + NFR) — *Done*
  - TASK-5.4 Metoda `analiza_zahteva` (ulančavanje 3 koraka) — *Done*

## EPIC-4 — Režim „Registar rizika" (workflow B)  *(Prioritet: High)*

- **US-6:** Kao menadžer rizika, želim registar rizika sa procenom (V×U) i merama.
  - TASK-6.1 Prompt B1 (komponente) — *Done*
  - TASK-6.2 Prompt B2 (identifikacija rizika) — *Done*
  - TASK-6.3 Prompt B3 (procena + registar + Top 3) — *Done*
  - TASK-6.4 Metoda `registar_rizika` (ulančavanje 3 koraka) — *Done*
- **US-7:** Kao korisnik, želim da se izlaz čuva kao Markdown, kako bih ga priložio dokumentaciji.
  - TASK-7.1 `sacuvaj_izlaz` sa vremenskom oznakom i metapodacima — *Done*

## EPIC-5 — Testiranje i validacija  *(Prioritet: Medium)*

- **US-8:** Kao developer, želim test na ≥3 ulaza, kako bih potvrdio da agent radi i da je izlaz strukturisan.
  - TASK-8.1 `test_agent.py` (3 ulaza × 2 režima) — *Done*
  - TASK-8.2 Automatska provera obaveznih sekcija — *Done*
- **US-9:** Kao developer, želim robusnu obradu grešaka, kako aplikacija ne bi pala.
  - TASK-9.1 Hvatanje grešaka modela (ključ/timeout/limit/konekcija) — *Done*

## EPIC-6 — Dokumentacija  *(Prioritet: Medium)*

- **US-10:** Kao komisija, želim projektni zadatak (SRS), kako bih ocenila obuhvat.
  - TASK-10.1 SRS dokument — *Done*
  - TASK-10.2 README (pokretanje) — *Done*
  - TASK-10.3 Kritička ocena (ograničenja/rizici/unapređenja) — *In Progress*
  - TASK-10.4 JIRA + GitHub povezivanje — *In Progress*

---

## Scrum/Kanban board (trenutni snapshot)

| To Do | In Progress | Review | Done |
|---|---|---|---|
| — | TASK-10.3, TASK-10.4 | — | EPIC-1..5 (sve), TASK-10.1, TASK-10.2 |

*Napomena:* board se popunjava u JIRA-i uvozom `3_JIRA_import.csv`, a screenshot table se prilaže uz seminarski (zahtev #12).
