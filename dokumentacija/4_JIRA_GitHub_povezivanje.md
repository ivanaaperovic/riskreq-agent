# Povezivanje JIRA ↔ GitHub (zahtev #13)

Cilj: prikazati kako se JIRA zadaci (npr. `RISKREQ-12`) povezuju sa GitHub aktivnostima
— granama, commit-ovima i Pull Request-ovima.

**Repozitorijum projekta:** https://github.com/ivanaaperovic/riskreq-agent

> Commit istorija već koristi konvenciju `RISKREQ-<broj>` u porukama (vidi `git log`),
> a ovaj dokument je dodat kroz granu `RISKREQ-13-jira-github` i Pull Request — što služi
> kao konkretan primer povezivanja JIRA zadatka sa GitHub aktivnostima.

---

## 1. Postavljanje GitHub repozitorijuma

```bash
cd ~/Documents/FON/upravljanje-rizikom/seminarski-ai-agent
git init
git add .
git commit -m "RISKREQ-1 Inicijalna struktura agenta"
git branch -M main
git remote add origin https://github.com/<korisnik>/riskreq-agent.git
git push -u origin main
```

> `.env` se NE commit-uje (već je u `.gitignore`). Commit-uje se `.env.example`.

## 2. Povezivanje JIRA i GitHub naloga

U JIRA Cloud-u (besplatan plan):

1. **Apps → Explore more apps → „GitHub for Jira"** (zvanična Atlassian integracija) → *Get app*.
2. Autorizovati GitHub nalog i izabrati repozitorijum `riskreq-agent`.
3. Od tada JIRA automatski prepoznaje **ključ issue-a** (npr. `RISKREQ-12`) u nazivima
   grana, commit porukama i PR-ovima i prikazuje ih u kartici issue-a (sekcija
   *Development*).

## 3. Konvencija: ključ issue-a u svemu

**Grana po user story / tasku:**
```bash
git checkout -b RISKREQ-6-registar-rizika
```

**Commit poruka sadrži ključ:**
```bash
git commit -m "RISKREQ-6 Dodat workflow B (komponente, rizici, procena V x U)"
git commit -m "RISKREQ-8 test_agent.py: test na 3 ulaza + provera sekcija"
```

**Pull Request naslov sadrži ključ:**
```
RISKREQ-6 Registar rizika — workflow B1->B2->B3
```

Kada se PR otvori/merge-uje, JIRA na kartici `RISKREQ-6` automatski prikaže granu,
commit-ove i PR, i može da pomeri status (npr. *In Progress → Done*) putem
*smart commits* (npr. `RISKREQ-6 #done`).

## 4. Primer mapiranja (za screenshot u radu)

| JIRA issue | GitHub grana | Primer commit-a | PR |
|---|---|---|---|
| RISKREQ-5 (US: user stories) | `RISKREQ-5-analiza-zahteva` | `RISKREQ-5 Workflow A: A1->A2->A3` | „RISKREQ-5 Analiza zahteva" |
| RISKREQ-6 (US: registar rizika) | `RISKREQ-6-registar-rizika` | `RISKREQ-6 Procena V x U + mere` | „RISKREQ-6 Registar rizika" |
| RISKREQ-8 (US: test) | `RISKREQ-8-testiranje` | `RISKREQ-8 test_agent.py 3 ulaza` | „RISKREQ-8 Testiranje" |

## 5. Smart commits (opciono, lepo za demo)

```bash
git commit -m "RISKREQ-8 #comment dodati testovi #time 2h #done"
```
- `#comment` → dodaje komentar na JIRA issue
- `#time 2h` → loguje vreme
- `#done` → menja status u Done

---

### Šta priložiti u seminarski (dokaz povezivanja)
1. Screenshot JIRA kartice sa vidljivom *Development* sekcijom (grana/commit/PR).
2. Screenshot GitHub liste grana sa imenima koja sadrže `RISKREQ-*`.
3. Link ka repozitorijumu.
