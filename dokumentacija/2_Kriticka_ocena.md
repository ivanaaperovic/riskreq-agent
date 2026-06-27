# Kritička ocena AI agenta „RiskReq"

Dokument prati zahtev #15 Grupe III: dokumentovati pokretanje i **kritički oceniti
korisnost** agenta — korišćene tehnologije, biblioteke, instalaciju, primer korišćenja,
**ograničenja, rizike korišćenja i mogućnosti za unapređenje**.

---

## 1. Korišćene tehnologije i biblioteke

| Sloj | Tehnologija |
|---|---|
| Jezik | Python 3.10+ |
| Orkestracija LLM-a | LangChain (`langchain-core`, `ChatPromptTemplate`, `StrOutputParser`) |
| LLM provajder | Ollama (`llama3.2`, lokalno) i/ili OpenAI (`gpt-4o-mini`) |
| Konfiguracija | `python-dotenv` (`.env`) |
| Opcioni izvor podataka | WooCommerce REST API (`woocommerce`, `requests`) |

**Instalacija i pokretanje:** detaljno u `README.md` (venv → `pip install -r requirements.txt`
→ `.env` → `python main.py`). Test: `python test_agent.py`.

## 2. Rezultati testiranja (zahtev #14)

Agent je testiran na **3 ulaza** (CreatorLab e-commerce, SkillSwap platforma, MobaBank
mobilno bankarstvo), svaki kroz **oba režima** = 6 pokretanja, sa lokalnim modelom
`llama3.2`. Svih 6 izlaza prošlo je automatsku **validaciju strukture** (`test_agent.py`):
sadrže sve propisane sekcije (user stories + acceptance criteria + NFR, odnosno registar
rizika sa procenom V×U + Top 3). Rezultati su u `izlaz/TEST_*.md`.

**Validacija sadržaja (ručna ocena):**

| Aspekt | Ocena | Komentar |
|---|---|---|
| Struktura izlaza | ✅ vrlo dobra | Sve sekcije prisutne, workflow vidljiv kroz 3 koraka. |
| Relevantnost stavki | ✅ dobra | Identifikovani akteri, celine i rizici odgovaraju ulazu (npr. za banku: autentikacija, regulativa, core banking). |
| Procena rizika (V×U) | ✅ smislena | Najviši nivoi dodeljeni bezbednosnim rizicima (chat, podaci, autentikacija). |
| Jezička ispravnost | ⚠️ osrednja | `llama3.2` povremeno klizi u hrvatske/rogobatne forme („vrijednost", „historiju", „svije finance"). |
| Doslednost tabele | ⚠️ povremeni propusti | Mali model ponekad izostavi ćeliju u redu tabele registra. |

## 3. Ograničenja

1. **Kvalitet zavisi od modela.** Sa lokalnim `llama3.2` (2 GB) jezik je rogobatan i
   povremeno netačan, a tabele ponekad imaju formatne propuste. Sa `gpt-4o-mini`/`gpt-4o`
   kvalitet i jezička ispravnost su znatno bolji (uz trošak i slanje podataka eksterno).
2. **Nema garancije tačnosti (halucinacije).** Agent može da „izmisli" rizik ili zahtev
   koji nije u ulazu, ili da propusti važan. Izlaz je **prvi nacrt**, ne konačan dokument.
3. **Plitka procena rizika.** V i U su procena LLM-a, bez kvantitativnih podataka (istorija
   incidenata, troškovi). Ne zamenjuje formalnu FMEA/kvantitativnu analizu.
4. **Ulaz ograničen na ~4000 karaktera** (chunking) — veliki dokumenti se skraćuju.
5. **CLI, bez perzistencije.** Svaki poziv je nezavisan; nema baze istorije ni
   uporedne analize verzija.
6. **Nedeterminizam.** Pri `temperature > 0` izlaz varira između pokretanja.

## 4. Rizici korišćenja agenta

| Rizik | Opis | Mera ublažavanja |
|---|---|---|
| Preterano poverenje u AI | Korisnik prihvati izlaz bez provere | Jasno označiti izlaz kao „nacrt za reviziju"; obavezna ljudska provera. |
| Curenje poverljivih podataka | Slanje internog opisa ka OpenAI | Koristiti lokalni Ollama za poverljive ulaze (agent to podržava bez izmene koda). |
| Lažan osećaj potpunosti | Lista rizika deluje kompletno, a nije | Tretirati kao polaznu listu; dopuniti domenskim znanjem. |
| Nekonzistentnost | Različiti izlazi za isti ulaz | Postaviti `LLM_TEMPERATURE=0` za ponovljivost. |

## 5. Mogućnosti za unapređenje

- **Strukturisani izlaz preko sheme** (Pydantic / `with_structured_output`) umesto
  slobodnog Markdown-a → eliminiše formatne propuste tabele.
- **RAG nad standardima** (ISO 31000, OWASP) da rizici budu utemeljeni u referencama.
- **Direktan export** registra u CSV/JIRA i priča u backlog (zatvoriti petlju ka JIRA).
- **Veb interfejs** (Streamlit) umesto CLI radi lakšeg demoa.
- **Evaluacioni sloj** (LLM-as-judge) koji ocenjuje sopstveni izlaz i traži dopune.
- **Podrazumevano jači model** za srpski jezik (npr. `gpt-4o`) uz lokalni fallback.

## 6. Zaključak

Agent ispunjava cilj Grupe III: rešava konkretan problem iz domena softverskog
inženjerstva i upravljanja rizikom, ima **jasno definisan ulaz, višekoračni workflow
(3 koraka), LLM komponentu i strukturisan izlaz**, i nije običan chatbot. Njegova prava
vrednost je u **ubrzavanju prvog nacrta** analize zahteva i registra rizika — uz obaveznu
ljudsku reviziju. Glavno ograničenje je kvalitet jezika lokalnog modela, što se rešava
prelaskom na jači model jednom linijom u `.env`.
