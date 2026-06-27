# RiskReq — AI agent za analizu zahteva i procenu rizika

AI agent (Python + **LangChain**) koji u procesu razvoja softvera automatizuje dva
zadatka product owner-a / menadžera rizika:

1. **Analiza zahteva** — iz tekstualnog opisa sistema generiše aktere, funkcionalne
   celine, **user stories** i **acceptance criteria** + kvantifikovane nefunkcionalne zahteve.
2. **Registar rizika** — iz opisa sistema identifikuje komponente i rizike, procenjuje ih
   (**Verovatnoća × Uticaj**) i predlaže mere ublažavanja.

Agent **nije chatbot**: za svaki ulaz izvršava **fiksiran workflow od 3 koraka** (izlaz
jednog koraka je ulaz sledećeg) i vraća **strukturisan Markdown izveštaj**.

> Seminarski rad, predmet *Upravljanje rizikom u razvoju aplikacija elektronskog
> poslovanja 2025/26*, Grupa III — Razvoj AI agenta. Tehnička osnova prilagođena iz
> ranijeg LangChain projekta (CreatorLab AI Agent) — zadržana arhitektura, promenjena namena.

---

## Workflow (2-3 koraka po režimu)

```
REŽIM 1 — Analiza zahteva
  A1  akteri + funkcionalne celine  ─►  A2  user stories  ─►  A3  acceptance criteria + NFR

REŽIM 2 — Registar rizika
  B1  ključne komponente/resursi    ─►  B2  rizici po komponenti  ─►  B3  procena (V×U) + mere
```

Svaki korak je zaseban LLM poziv (`prompt | model | parser`), pa je vidljiv tok obrade
od ulaza do strukturisanog izlaza.

---

## Struktura projekta

```
seminarski-ai-agent/
├── main.py               # ulazna tačka: meni, izbor modela/režima/izvora, čuvanje izlaza
├── config.py             # učitavanje .env, validacija, lista modela
├── data_processing.py    # priprema ulaza: čišćenje, chunking, (opciono) WooCommerce
├── llm_provider.py       # fabrika za LLM (Ollama / OpenAI)
├── prompts.py            # višekoračni promptovi (A1–A3, B1–B3)
├── agent.py              # AI logika: workflow od 3 koraka po režimu
├── woocommerce_client.py # opcioni izvor podataka (CreatorLab prodavnica)
├── test_agent.py         # test na ≥3 ulaza + validacija strukture izlaza
├── ulaz/                 # primeri ulaza (.txt)
├── izlaz/                # generisani izveštaji (.md)
├── dokumentacija/        # projektni zadatak (SRS), kritička ocena, JIRA/GitHub
├── requirements.txt
└── .env.example
```

---

## Pokretanje

### 1. Zavisnosti

```bash
cd ~/Documents/FON/upravljanje-rizikom/seminarski-ai-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Konfiguracija (`.env`)

Kopiraj `.env.example` u `.env` i izaberi provajdera.

**A) Ollama (besplatno, lokalno — podrazumevano):**
```
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2
```
Preduslov:
```bash
brew install ollama
brew services start ollama
ollama pull llama3.2
```

**B) OpenAI (bolji kvalitet izlaza, traži ključ):**
```
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...tvoj-kljuc...
OPENAI_MODEL=gpt-4o-mini
```

WooCommerce ključevi su **opcioni** — potrebni samo za izvor „povuci CreatorLab prodavnicu".

### 3. Pokretanje agenta

```bash
python main.py
```

Tok: izbor modela → meni (1 Analiza zahteva / 2 Registar rizika) → izbor izvora ulaza
(unos / fajl iz `ulaz/` / WooCommerce) → agent izvrši 3 koraka → rezultat se prikaže i
sačuva u `izlaz/`.

### 4. Test na 3 ulaza (validacija)

```bash
python test_agent.py
```
Propušta sva 3 ulaza iz `ulaz/` kroz oba režima, čuva `TEST_*.md` u `izlaz/` i ispisuje
koliko izlaza ima sve očekivane sekcije.

---

## Potrebne biblioteke
`langchain`, `langchain-core`, `langchain-ollama` (i/ili `langchain-openai`),
`python-dotenv`; opciono `woocommerce`, `requests`. Sve u `requirements.txt`.

## Dokumentacija
- `dokumentacija/1_Projektni_zadatak_SRS_Agent_Ivana_Perovic.md` — projektni zadatak (SRS).
- `dokumentacija/2_Kriticka_ocena.md` — ograničenja, rizici korišćenja, unapređenja.
- `dokumentacija/3_JIRA_projekat.md` — epike / user stories / taskovi (+ CSV za import).
- `dokumentacija/4_JIRA_GitHub_povezivanje.md` — povezivanje JIRA ↔ GitHub.
