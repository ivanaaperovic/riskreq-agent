# JIRA — korak po korak (uputstvo za izradu i screenshot-ove)

Ovo je praktično uputstvo da napraviš JIRA projekat za agenta i prikupiš screenshot-ove
koji se prilažu u seminarski (zahtevi #12 — JIRA projekat + board, i #13 — JIRA↔GitHub).

Repozitorijum: https://github.com/ivanaaperovic/riskreq-agent
Fajl za uvoz: `dokumentacija/3_JIRA_import.csv`

---

## 0. Nalog (jednom)

1. Otvori https://www.atlassian.com/software/jira → **Get it free** (besplatan plan do 10 korisnika).
2. Prijavi se Google nalogom (`ivanaaperovicc@gmail.com`) ili napravi nalog.
3. Dobićeš svoj sajt tipa `https://ivana-xxxx.atlassian.net`.

---

## 1. Kreiranje projekta

1. Gore levo **Projects → Create project**.
2. Izaberi šablon **Scrum** (Software development) → **Use template** → **Next**.
3. Naziv projekta: **RiskReq Agent**; ključ (key) postavi na **RISKREQ**.
   - *Bitno:* ključ MORA biti `RISKREQ` jer se commit-ovi (`RISKREQ-1`, `RISKREQ-5`…) već
     oslanjaju na njega.
4. **Create**.

📸 **Screenshot 1:** ekran sa nazivom projekta i ključem `RISKREQ` pre klika na Create.

---

## 2. Uvoz epika/priča/taskova iz CSV-a

> Najbrži način — uveze sve odjednom iz `3_JIRA_import.csv`.

1. Gore desno (zupčanik) **⚙ Settings → System**.
2. U levom meniju (sekcija *Import and Export*) → **External System Import**.
3. Izaberi **CSV** → **Choose File** → izaberi
   `~/Documents/FON/upravljanje-rizikom/seminarski-ai-agent/dokumentacija/3_JIRA_import.csv`.
4. Na pitanje za projekat izaberi **RiskReq Agent (RISKREQ)**.
5. **Map fields** — poveži kolone (JIRA obično sam prepozna):
   - `Issue Type` → Issue Type
   - `Summary` → Summary
   - `Epic Name` → Epic Name
   - `Epic Link` → Epic Link
   - `Parent` → Parent (za taskove ispod priča)
   - `Priority` → Priority
   - `Status` → Status
   - `Assignee` → Assignee (ako traži, mapiraj na svoj nalog)
   - `Description` → Description
6. **Next → Begin Import**.

📸 **Screenshot 2:** poruka „X issues imported successfully".

> **Ako CSV uvoz pravi problem** (neki besplatni planovi kriju External System Import):
> napravi bar **6 epika + 10 priča + nekoliko taskova ručno** prema
> `dokumentacija/3_JIRA_projekat.md` (tabela je tu, samo prekucaš). Za ocenu je dovoljno
> da se vidi hijerarhija epic → story → task i statusi.

---

## 3. Backlog i board

1. Levi meni → **Backlog**: videćeš sve priče i taskove grupisane po epikama.
   - Otvori panel **Epics** (levo) da se vidi obojena podela po epikama.

📸 **Screenshot 3:** Backlog sa vidljivim epikama i pričama.

2. Prevuci nekoliko stavki u **Sprint 1** → klikni **Start sprint** (trajanje stavi 2 nedelje, samo da se aktivira board).
3. Levi meni → **Board**: kolone **To Do / In Progress / Done**.
   - Prevuci par taskova u *In Progress* i *Done* da board ne bude prazan (kao u
     `3_JIRA_projekat.md`: EPIC-1..5 = Done, dokumentacija = In Progress).
   - *(Opciono)* dodaj kolonu **Review**: Board → ⚙ (Configure board) → Columns → Add column.

📸 **Screenshot 4:** Board sa zadacima u kolonama (To Do / In Progress / (Review) / Done).

---

## 4. Povezivanje sa GitHub-om (zahtev #13)

1. Gore **Apps → Explore more apps** → pretraži **„GitHub for Jira"** (Atlassian, zvanično) → **Get app / Install**.
2. Prati čarobnjak: **Connect GitHub account** → autorizuj nalog **ivanaaperovic** →
   izaberi repo **riskreq-agent** → **Connect**.
3. Sačekaj da JIRA povuče commit istoriju (par minuta).
4. Otvori bilo koji issue čiji se ključ pojavljuje u commit-u, npr. **RISKREQ-5** ili
   **RISKREQ-8** → na kartici se pojavi sekcija **Development** sa granom/commit-om/PR-om.

📸 **Screenshot 5:** kartica issue-a `RISKREQ-13` (ili `RISKREQ-5`) sa vidljivom
**Development** sekcijom (commit + grana `RISKREQ-13-jira-github` + Pull Request #1).

📸 **Screenshot 6 (sa GitHub-a):** lista grana / PR #1 na
https://github.com/ivanaaperovic/riskreq-agent — kao dokaz konvencije `RISKREQ-*`.

> Veza radi jer commit poruke već sadrže ključeve (`git log` to pokazuje), a grana i
> PR #1 su napravljeni baš pod `RISKREQ-13`.

---

## 5. Šta tačno ide u seminarski (čeklista screenshot-ova)

| # | Screenshot | Pokriva zahtev |
|---|---|---|
| 1 | Kreiranje projekta (ključ RISKREQ) | #12 |
| 2 | Uspešan uvoz / lista issue-a | #12 |
| 3 | Backlog sa epikama i pričama | #12 |
| 4 | Board (To Do/In Progress/Done) | #12 |
| 5 | Issue kartica sa Development (commit/grana/PR) | #13 |
| 6 | GitHub grane/PR sa `RISKREQ-*` | #13 |

Kad prikupiš ove screenshot-ove, ubaci ih u glavni dokument seminarskog (uz tekst iz
`3_JIRA_projekat.md` i `4_JIRA_GitHub_povezivanje.md`) i time su zahtevi #12 i #13 zatvoreni.
