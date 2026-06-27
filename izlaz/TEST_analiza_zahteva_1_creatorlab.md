<!-- Test: 1_creatorlab.txt | rezim: analiza_zahteva | model: llama3.2 | 2026-06-27 11:58 -->

# Analiza zahteva

## Korak 1 — Akteri i funkcionalne celine

### Akteri
#### 1. Posetilac
Korisnik koji pregledava katalog kurseva i dodaje kurs u korpu, a zatim pristupuje video lekcijama.

#### 2. Registrovani polaznik
Korisnik koji je registrovan na aplikaciji i ima pristup video lekcijama po odabranim kursem.

#### 3. Administrator
Korisnik sa posebnim pristupom koji dodaje kurseve, cene i opise, prati prodaju i cuva podatke o korisnicima.

### Funkcionalne celine
1. Dodavanje kursa
2. Pregled kataloga kurseva
3. Dodavanje kursa u korpu
4. Placanje karticom
5. Dobivanje pristupa video lekcijama
6. Prirucivanje administratora za dodavanje kurseva i cene
7. Salje email potvrde o kupovini
8. Cuva podatke o korisnicima

## Korak 2 — User stories

### Akteri
#### 1. Posetilac
Korisnik koji pregledava katalog kurseva i dodaje kurs u korpu, a zatim pristupuje video lekcijama.

#### 2. Registrovani polaznik
Korisnik koji je registrovan na aplikaciji i ima pristup video lekcijama po odabranim kursem.

#### 3. Administrator
Korisnik sa posebnim pristupom koji dodaje kurseve, cene i opise, prati prodaju i cuva podatke o korisnicima.

### Funkcionalne celine

1. **Dodavanje kursa**
   - **US-1:** Kao administrator, zelim da mogu dodati novi kurs u sistem.
   - **US-2:** Kao administrator, zelim da mogu urediti detalje postojećih kurseva.

2. **Pregled kataloga kurseva**
   - **US-3:** Kao posetilac, zelim da mogu pregledati katalog kurseva i vidjeti informacije o svakom kursu.
   - **US-4:** Kao registrovani polaznik, zelim da mogu pregledati katalog kurseva i vidjeti informacije o svakom kursu.

3. **Dodavanje kursa u korpu**
   - **US-5:** Kao posetilac, zelim da mogu dodati kurs u korpu.
   - **US-6:** Kao registrovani polaznik, zelim da mogu dodati kurs u korpu.

4. **Placanje karticom**
   - **US-7:** Kao posetilac, zelim da mogu platiti kurs karticom.
   - **US-8:** Kao administrator, zelim da mogu prati prodaju i vidjeti informacije o plaćenim kupovinama.

5. **Dobivanje pristupa video lekcijama**
   - **US-9:** Kao registrovani polaznik, zelim da mogu dobiti pristup video lekcijama po odabranom kursem.
   - **US-10:** Kao administrator, zelim da mogu prirucavati korisnike za pristup video lekcijama.

6. **Prirucivanje administratora za dodavanje kurseva i cene**
   - **US-11:** Kao administrator, zelim da mogu prirucavati detalje o postojećim kursima.
   - **US-12:** Kao administrator, zelim da mogu dodati novi kurs u sistem.

7. **Salje email potvrde o kupovini**
   - **US-13:** Kao sistema, zelim da saljem email potvrde o kupovini korisnicima.
   - **US-14:** Kao administrator, zelim da mogu prati prodaju i vidjeti informacije o plaćenim kupovinama.

8. **Cuva podatke o korisnicima**
   - **US-15:** Kao sistem, zelim da cujem informacije o korisnicima (ime, email, istorija kupovina).
   - **US-16:** Kao administrator, zelim da mogu prirucavati detalje o korisnicima.

## Korak 3 — Acceptance criteria i nefunkcionalni zahtevi

## User stories sa acceptance criteria
### Akteri
#### 1. Posetilac
Korisnik koji pregledava katalog kurseva i dodaje kurs u korpu, a zatim pristupuje video lekcijama.

* **US-1:** Kao posetilac, zelim da mogu pregledati katalog kurseva i vidjeti informacije o svakom kursu.
	+ **AC-1.1:** Pregledajmo katalog kurseva i vidjetimo informacije o svakom kursu (naslov, opis, cijena).
	+ **AC-1.2:** Pregledajmo korpu i vidjetimo dodane kurseve.
* **US-2:** Kao posetilac, zelim da mogu dodati kurs u korpu.
	+ **AC-2.1:** Dodajmo kurs u korpu izabranih kursea.
	+ **AC-2.2:** Pregledajmo korpu i vidjetimo dodane kurseve.

#### 2. Registrovani polaznik
Korisnik koji je registrovan na aplikaciji i ima pristup video lekcijama po odabranim kursem.

* **US-3:** Kao registrovani polaznik, zelim da mogu pregledati katalog kurseva i vidjeti informacije o svakom kursu.
	+ **AC-3.1:** Pregledajmo katalog kurseva i vidjetimo informacije o svakom kursu (naslov, opis, cijena).
	+ **AC-3.2:** Pregledajmo korpu i vidjetimo dodane kurseve.
* **US-4:** Kao registrovani polaznik, zelim da mogu pregledati katalog kurseva i vidjeti informacije o svakom kursu.
	+ **AC-4.1:** Pregledajmo katalog kurseva i vidjetimo informacije o svakom kursu (naslov, opis, cijena).
	+ **AC-4.2:** Pregledajmo korpu i vidjetimo dodane kurseve.

#### 3. Administrator
Korisnik sa posebnim pristupom koji dodaje kurseve, cene i opise, prati prodaju i cuva podatke o korisnicima.

* **US-5:** Kao administrator, zelim da mogu dodati novi kurs u sistem.
	+ **AC-5.1:** Dodajmo novi kurs u sistem sa informacijama (naslov, opis, cijena).
	+ **AC-5.2:** Pregledajmo katalog kurseva i vidjetimo dodane kurseve.
* **US-6:** Kao administrator, zelim da mogu urediti detalje postojećih kurseva.
	+ **AC-6.1:** Uredimo detalje postojećih kurseva (naslov, opis, cijena).
	+ **AC-6.2:** Pregledajmo katalog kurseva i vidjetimo uredene kurseve.

## Funkcionalne celine

### Dodavanje kursa
* **US-7:** Kao administrator, zelim da mogu dodati novi kurs u sistem.
	+ **AC-7.1:** Dodajmo novi kurs u sistem sa informacijama (naslov, opis, cijena).
	+ **AC-7.2:** Pregledajmo katalog kurseva i vidjetimo dodane kurseve.

### Pregled kataloga kurseva
* **US-8:** Kao administrator, zelim da mogu pregledati katalog kurseva i vidjeti informacije o svakom kursu.
	+ **AC-8.1:** Pregledajmo katalog kurseva i vidjetimo informacije o svakom kursu (naslov, opis, cijena).
	+ **AC-8.2:** Pregledajmo korpu i vidjetimo dodane kurseve.

### Dodavanje kursa u korpu
* **US-9:** Kao posetilac, zelim da mogu dodati kurs u korpu.
	+ **AC-9.1:** Dodajmo kurs u korpu izabranih kursea.
	+ **AC-9.2:** Pregledajmo korpu i vidjetimo dodane kurseve.

### Placanje karticom
* **US-10:** Kao posetilac, zelim da mogu platiti kurs karticom.
	+ **AC-10.1:** Platimo kurs karticom izabranih kursea.
	+ **AC-10.2:** Pregledajmo korpu i vidjetimo dodane kurseve.

### Dobivanje pristupa video lekcijama
* **US-11:** Kao registrovani polaznik, zelim da mogu dobiti pristup video lekcijama po odabranom kursem.
	+ **AC-11.1:** Dobićemo pristup video lekcijama po odabranom kursem.
	+ **AC-11.2:** Pregledajmo korpu i vidjetimo dodane kurseve.

### Prirucivanje administratora za dodavanje kurseva i cene
* **US-12:** Kao administrator, zelim da mogu prirucavati detalje o postojećim kursima.
	+ **AC-12.1:** Uredimo detalje o postojećim kursima (naslov, opis, cijena).
	+ **AC-12.2:** Pregledajmo katalog kurseva i vidjetimo uredene kurseve.

### Salje email potvrde o kupovini
* **US-13:** Kao sistema, zelim da saljem email potvrde o kupovini korisnicima.
	+ **AC-13.1:** Saljemo email potvrde o kupovini korisnicima.
	+ **AC-13.2:** Pregledajmo korpu i vidjetimo dodane kurseve.

### Cuva podatke o korisnicima
* **US-14:** Kao administrator, zelim da mogu prirucavati detalje o korisnicima.
	+ **AC-14.1:** Uredimo detalje o korisnicima (ime, email, istorija kupovina).
	+ **AC-14.2:** Pregledajmo katalog korisnika i vidjetimo detalje o svim korisnicima.

## Nefunkcionalni zahtevi

| Kategorija | Zahtev | Merljiva meta |
| --- | --- | --- |
| Performans | Odziv < 2s | - |
| Sigurnost | Lozinke hesirane bcrypt | - |
| Dostupnost | Dostupnost >= 99% | - |
| Kvalitet | Korisnik mora imati pristup video lekcijama po odabranom kursem | - |
| Funkcionalnost | Sustav mora moći dodati i urediti kursove | - |

Napomena: Merljiva meta označava da je zahtev merljiv i da se može proceniti kao uspjeh ili neuspjeh sistema.
