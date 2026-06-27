<!-- Test: 2_skillswap.txt | rezim: registar_rizika | model: llama3.2 | 2026-06-27 12:05 -->

# Procena rizika

## Korak 1 — Kljucne komponente i resursi

### Kljucne komponente i resurse

1. **Baza**:
	* Baza podataka za korisnike, profile i vestine
	* Baza kredita za razmenu vestina
2. **Autentikacija**:
	* Sistemu autentičiranje korisnika (npr. login, password)
3. **Placanje**:
	* Interne kredite koje se koriste za razmenu vestina
4. **Eksterni servisi**:
	* API za integraciju sa drugim servisima (npr. social media)
5. **Podaci o korisnicima**:
	* Profili korisnika, njihove ocene i recenzije
6. **Integracije**:
	* Integracija s kalendarem za zakazivanje termina
7. **Chat**:
	* Chat izmedju korisnika
8. **Notifikacije**:
	* Notifikacije o novim zahtjevima, ocenama i recenzijama
9. **Sistem moderiranja**:
	* Sistem za moderiranje prijave neprimerenog ponasanja

Ove ključne komponente i resurse su bitne za rizik u razvoju SkillSwap platforme.

## Korak 2 — Identifikovani rizici

### Identifikovani rizici

#### 1. Baza
* **R-1:** Brisanje ili korupcija podataka u bazi, što može dovesti do neprekidnog rada platforme.
	+ Komponenta: Baza podataka za korisnike, profile i vestine
	+ Kategorija: Tehnički

#### 2. Autentikacija
* **R-2:** Nepokvarena autentična sistema ili krštenje korisnika, što može dovesti do neprekidnog rada platforme.
	+ Komponenta: Sistemu autentičiranje korisnika (npr. login, password)
	+ Kategorija: Tehnički

#### 3. Placanje
* **R-3:** Nepokvarena razmena vestina ili neefikasnost sistema kredita, što može dovesti do neprekidnog rada platforme.
	+ Komponenta: Interne kredite koje se koriste za razmenu vestina
	+ Kategorija: Tehnički

#### 4. Eksterni servisi
* **R-4:** Nepokvarena integracija sa drugim servisima (npr. social media), što može dovesti do neprekidnog rada platforme.
	+ Komponenta: API za integraciju sa drugim servisima (npr. social media)
	+ Kategorija: Tehnički

#### 5. Podaci o korisnicima
* **R-5:** Nepokvarena bezbednost podataka o korisnicima, što može dovesti do neprekidnog rada platforme.
	+ Komponenta: Profili korisnika, njihove ocene i recenzije
	+ Kategorija: Bezbednosne

#### 6. Integracije
* **R-6:** Nepokvarena integracija s kalendarem za zakazivanje termina, što može dovesti do neprekidnog rada platforme.
	+ Komponenta: Integracija s kalendarem za zakazivanje termina
	+ Kategorija: Tehnički

#### 7. Chat
* **R-7:** Nepokvarena bezbednost u chatu, što može dovesti do neprekidnog rada platforme.
	+ Komponenta: Chat izmedju korisnika
	+ Kategorija: Bezbednosne

#### 8. Notifikacije
* **R-8:** Nepokvarena implementacija notifikacija, što može dovesti do neprekidnog rada platforme.
	+ Komponenta: Notifikacije o novim zahtjevima, ocenama i recenzijama
	+ Kategorija: Tehnički

#### 9. Sistem moderiranja
* **R-9:** Nepokvarena implementacija sistema moderiranja prijave neprimerenog ponasanja, što može dovesti do neprekidnog rada platforme.
	+ Komponenta: Sistem za moderiranje prijave neprimerenog ponasanja
	+ Kategorija: Tehnički

## Korak 3 — Registar rizika i prioriteti

## Registar rizika

| ID | Rizik | Kategorija | V (Verovatnoca) | U (Uticaj) | Nivo (VxU) | Ocena | Strategija | Mera ublazavanja |
|----|-------|-----------|---------------|-----------|-----------|-------|-----------|------------------|
|R-1| Brisanje ili korupcija podataka u bazi| Tehnički| 3          | 4         | 12       | Visok   | Prihvatanje| Implementacija redizajna sistema za podršku baze podataka |
|R-2| Nepokvarena autentična sistema ili krštenje korisnika| Tehnički| 4          | 5         | 20       | Kritican| Implementacija novog sistema autentičiranja korisnika i krštenja |
|R-3| Nepokvarena razmena vestina ili neefikasnost sistema kredita| Tehnički| 3          | 4         | 12       | Visok   | Implementacija novog sistema razmeđe vestina i efikasnosti sistema kredita |
|R-4| Nepokvarena integracija sa drugim servisima| Tehnički| 2          | 3         | 6        | Nizak  | Izbegavanje| Pretraga alternativnih servisa za integraciju |
|R-5| Nepokvarena bezbednost podataka o korisnicima| Bezbednosne| 4          | 5         | 20       | Kritican| Implementacija novog sistema za podršku bezbednosti podataka o korisnicima |
|R-6| Nepokvarena integracija s kalendarem za zakazivanje termina| Tehnički| 3          | 4         | 12       | Visok   | Implementacija novog sistema integracije s kalendarem za zakazivanje termina |
|R-7| Nepokvarena bezbednost u chatu| Bezbednosne| 5          | 5         | 25       | Kritican| Implementacija novog sistema za podršku bezbednosti u chatu |
|R-8| Nepokvarena implementacija notifikacija| Tehnički| 2          | 3         | 6        | Nizak  | Izbegavanje| Pretraga alternativnih servisa za implementaciju notifikacija |
|R-9| Nepokvarena implementacija sistema moderiranja prijave neprimerenog ponasanja| Tehnički| 4          | 5         | 20       | Kritican| Implementacija novog sistema moderiranja prijave neprimerenog ponasanja |

## Top 3 prioritetna rizika

1. **R-2: Nepokvarena autentična sistema ili krštenje korisnika** - Ova rizika je kritično jer može dovesti do neprekidnog rada platforme i kompromitisanja bezbednosti podataka o korisnicima.
2. **R-5: Nepokvarena bezbednost podataka o korisnicima** - Ova rizika je kritično jer može dovesti do neprekidnog rada platforme i kompromitisanja privatnosti korisnika.
3. **R-9: Nepokvarena implementacija sistema moderiranja prijave neprimerenog ponasanja** - Ova rizika je kritično jer može dovesti do neprekidnog rada platforme i kompromitisanja bezbednosti korisnika.

Ove tri rizika su prioritetni jer imaju najveći uticaj na funkcioniranje platforme i bezbednost korisnika.
