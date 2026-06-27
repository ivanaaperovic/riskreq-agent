<!-- Test: 2_skillswap.txt | rezim: analiza_zahteva | model: llama3.2 | 2026-06-27 12:03 -->

# Analiza zahteva

## Korak 1 — Akteri i funkcionalne celine

### Akteri

* Korisnik: kreira profil, navodi vestine koje nudi i trazi, pretrazuje druge korisnike, salje zahtev za razmenu i zakazuje termin.
* Administrator: moderira prijave neprimerenog ponasanja i upravlja kategorijama vestina.

### Funkcionalne celine

1. Profil kreiraške
2. Pretraga korisnika
3. Nudjenje i traženje vestina
4. Salje zahtev za razmenu
5. Zakazivanje termina
6. Sistem kredita
7. Kalendar termina
8. Chat izmedju korisnika
9. Notifikacije
10. Moderacija prijave neprimerenog ponasanja
11. Upravljanje kategorijama vestina

## Korak 2 — User stories

### Korisnik: Kreira profil, navodi vestine koje nudi i trazi, pretrazuje druge korisnike, salje zahtev za razmenu i zakazuje termin.

* US-1: Kao korisnik, zelim da mogu kreativno izglasati svoje profile kako bi se razlikovao od drugih korisnika.
* US-2: Kao korisnik, zelim da mogu navoditi vestine koje nudi i trazi kako bi moglo da se razume koji suvestine potrebne za koga.
* US-3: Kao korisnik, zelim da mogu pretraziti druge korisnike kako bi moglo da se pronađe ljudi sa interesom za određenu vestina.

### Funkcionalne celine

1. Profil kreiraške
2. Pretraga korisnika
3. Nudjenje i traženje vestina
4. Salje zahtev za razmenu
5. Zakazivanje termina
6. Sistem kredita
7. Kalendar termina
8. Chat izmedju korisnika
9. Notifikacije

### Administrator: Moderira prijave neprimerenog ponasanja i upravlja kategorijama vestina.

* US-10: Kao administrator, zelim da mogu moderisati prijave koji su neprimerene kako bi se sprečio nepotreban sadržaj.
* US-11: Kao administrator, zelim da mogu upravljati kategorije vestina kako bi se osiguralo da sve sadržaji budu relevantni i korisni.

## Korak 3 — Acceptance criteria i nefunkcionalni zahtevi

## User stories sa acceptance criteria

### Korisnik: Kreira profil, navodi vestine koje nudi i trazi, pretrazuje druge korisnike, salje zahtev za razmenu i zakazuje termin.

#### US-1: Kao korisnik, zelim da mogu kreativno izglasati svoje profile kako bi se razlikovao od drugih korisnika.
* **Given**: Korisnik je prijavljen u sistem
* **When**: Korisnik izabere izbor za svoj profil
* **Then**: Profil korisnika sadrži izabrane slike i opise koji su različiti od ostalih korisnika

#### US-2: Kao korisnik, zelim da mogu navoditi vestine koje nudi i trazi kako bi moglo da se razume koji suvestine potrebne za koga.
* **Given**: Korisnik je prijavljen u sistem
* **When**: Korisnik unese naziv i opis vestine
* **Then**: Vestina je spremljena sa korisnikom u svojoj profili

#### US-3: Kao korisnik, zelim da mogu pretraziti druge korisnike kako bi moglo da se pronađe ljudi sa interesom za određenu vestina.
* **Given**: Korisnik je prijavljen u sistem
* **When**: Korisnik unese naziv i opis vestine koju traži
* **Then**: Rezultati pretrage sadrže korisnike koji su tražilivestinu

### Funkcionalne celine

1. Profil kreiraške
2. Pretraga korisnika
3. Nudjenje i traženje vestina
4. Salje zahtev za razmenu
5. Zakazivanje termina
6. Sistem kredita
7. Kalendar termina
8. Chat izmedju korisnika
9. Notifikacije

#### 1. Profil kreiraške
* **Given**: Korisnik je prijavljen u sistem
* **When**: Korisnik izabere izbor za svoj profil
* **Then**: Profil korisnika je stvoren i spremljen u bazu podataka

#### 2. Pretraga korisnika
* **Given**: Korisnik je prijavljen u sistem
* **When**: Korisnik unese naziv ili opis korisnike koji traži
* **Then**: Rezultati pretrage sadrže korisnike koji su tražilivestinu

#### 3. Nudjenje i traženje vestina
* **Given**: Korisnik je prijavljen u sistem
* **When**: Korisnik unese naziv ili opis vestine koju traži ili nudi
* **Then**: Rezultati pretrage sadrže korisnike koji su tražilivestinu ili korisnike koji su nudivestinu

#### 4. Salje zahtev za razmenu
* **Given**: Korisnik je prijavljen u sistem i ima aktivan profil
* **When**: Korisnik salje zahtev za razmenu korisniku ili vestini
* **Then**: Zahtev je spremljen u bazu podataka

#### 5. Zakazivanje termina
* **Given**: Korisnik je prijavljen u sistem i ima aktivan profil
* **When**: Korisnik zakazuje termin za razmenu ili vestinu
* **Then**: Termin je spremljen u bazu podataka

#### 6. Sistem kredita
* **Given**: Korisnik je prijavljen u sistem i ima aktivan profil
* **When**: Korisnik koristi sistem za zakazivanje termina ili zahtev za razmenu
* **Then**: Korisnik dobija poeni ili kredite

#### 7. Kalendar termina
* **Given**: Korisnik je prijavljen u sistem i ima aktivan profil
* **When**: Korisnik pristupi kalendaru termina
* **Then**: Kalendar pokazuje sve zakazane terminove za korisnika

#### 8. Chat izmedju korisnika
* **Given**: Korisnik je prijavljen u sistem i ima aktivan profil
* **When**: Korisnik pristupi chatu sa drugim korisnikom
* **Then**: Korisnik može da komunicira sa drugim korisnikom

#### 9. Notifikacije
* **Given**: Korisnik je prijavljen u sistem i ima aktivan profil
* **When**: Korisnik primi notifikaciju za neki događaj (npr. novi zahtev za razmenu)
* **Then**: Korisnik primi notifikaciju

### Administrator: Moderira prijave neprimerenog ponasanja i upravlja kategorijama vestina.

#### US-10: Kao administrator, zelim da mogu moderisati prijave koji su neprimerene kako bi se sprečio nepotreban sadržaj.
* **Given**: Administrator je prijavljen u sistem
* **When**: Administrator pristupi prijavama koje su neprimerene
* **Then**: Administrator može da moderira i sprema prijave koji su neprimerene

#### US-11: Kao administrator, zelim da mogu upravljati kategorijama vestina kako bi se osiguralo da sve sadržaji budu relevantni i korisni.
* **Given**: Administrator je prijavljen u sistem
* **When**: Administrator pristupi kategorijama vestina
* **Then**: Administrator može da upravlja i modificira kategorije vestina
