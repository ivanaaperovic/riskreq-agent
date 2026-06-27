<!-- Test: 3_mobilno_bankarstvo.txt | rezim: analiza_zahteva | model: llama3.2 | 2026-06-27 12:09 -->

# Analiza zahteva

## Korak 1 — Akteri i funkcionalne celine

### Akteri
#### Korisnik
Korisnik je osoba koja koristi aplikaciju MobaBank za upravljanje racunima. On se prijavljuje korisnickim imenom i lozinkom, a transakcije potvrdjuje biometrijom ili jednokratnim kodom.

#### Administrator
Administrator je osoba koja upravlja aplikacijom MobaBank i core banking sistemom banke. On salje informacije o korisnicima i transakcijama, kao i radi sa regulativnom kontrolom.

### Funkcionalne celine
1. Pregled stanja i prometa po racunima
2. Instant placanje i prenos sredstava
3. Placanje racuna skeniranjem QR/IPS koda
4. Otvaranje stednje
5. Blokada kartice
6. Podesavanje limita
7. Saljivanje push notifikacija o transakcijama

## Korak 2 — User stories

### Korisnik
#### Pregled stanja i prometa po racunima
- **US-1:** Kao korisnik, zelim pristup pregledu stanja i prometa po svom racunu kako bih vidio trenutni stanje i historiju transakcija.
- **US-2:** Kao korisnik, zelim da mogu pristupiti detaljnim informacijama o svim transakcijama, kao što su datum, vrijednost i opis transakcije.

#### Instant placanje i prenos sredstava
- **US-3:** Kao korisnik, zelim da mogu izvršiti instant placanje i prenos sredstava kako bih brzo i lako obavljao financijske transakcije.
- **US-4:** Kao korisnik, zelim da mogu pristupiti detaljnim informacijama o svim prenosima sredstava, kao što su datum, vrijednost i opis transakcije.

#### Placanje racuna skeniranjem QR/IPS koda
- **US-5:** Kao korisnik, zelim da mogu platiti racunama skeniranjem QR/IPS koda kako bih brzo i lako obavljao financijske transakcije.
- **US-6:** Kao korisnik, zelim da mogu pristupiti detaljnim informacijama o svim platnjama racunama, kao što su datum, vrijednost i opis transakcije.

#### Otvaranje stednje
- **US-7:** Kao korisnik, zelim da mogu otvoriti stednju kako bih pristupio svim racunima koji su u stednju.
- **US-8:** Kao korisnik, zelim da mogu pristupiti detaljnim informacijama o svim stednjima, kao što su datum i opis stednje.

#### Blokada kartice
- **US-9:** Kao korisnik, zelim da mogu blokirati karticu kako bih zaštitio svije finance.
- **US-10:** Kao korisnik, zelim da mogu pristupiti detaljnim informacijama o blokiranoj kartici, kao što su datum i opis razloga.

#### Podesavanje limita
- **US-11:** Kao korisnik, zelim da mogu podesavati limite racuna kako bih kontrolirao svije finance.
- **US-12:** Kao korisnik, zelim da mogu pristupiti detaljnim informacijama o svim podesavanima limita, kao što su datum i opis promjene.

#### Saljivanje push notifikacija o transakcijama
- **US-13:** Kao korisnik, zelim da primam push notifikacije o svim transakcijama kako bih bio upozoren za sve finance.
- **US-14:** Kao korisnik, zelim da mogu pristupiti detaljnim informacijama o svim notifikacijama, kao što su datum i opis transakcije.

### Administrator
#### Saljivanje informacija o korisnicima i transakcijama
- **US-15:** Kao administrator, zelim da mogu saljiti informacije o korisnicima i transakcijama kako bih upozorio se za sve finance.
- **US-16:** Kao administrator, zelim da mogu pristupiti detaljnim informacijama o svim korisnicima i transakcijama, kao što su datum i opis aktivnosti.

#### Saljivanje push notifikacija o transakcijama
- **US-17:** Kao administrator, zelim da mogu saljiti push notifikacije o transakcijama kako bih upozorio se za sve finance.
- **US-18:** Kao administrator, zelim da mogu pristupiti detaljnim informacijama o svim notifikacijama, kao što su datum i opis transakcije.

#### Kontrola regulativne kontrolne
- **US-19:** Kao administrator, zelim da mogu kontrolirati sve finance kako bih siguran da se sreću s regulativnim standardima.
- **US-20:** Kao administrator, zelim da mogu pristupiti detaljnim informacijama o svim kontrolama, kao što su datum i opis aktivnosti.

## Korak 3 — Acceptance criteria i nefunkcionalni zahtevi

## User stories sa acceptance criteria

### Korisnik
#### Pregled stanja i prometa po racunima
- **US-1:** Kao korisnik, zelim pristup pregledu stanja i prometa po svom racunu kako bih vidio trenutni stanje i historiju transakcija.
	+ **AC-1.1:** Pregledajmo trenutno stanje racuna u realnom vremenu.
	+ **AC-1.2:** Pogledajmo historiju transakcija za svaki racun.
	+ **AC-1.3:** Uključite detaljne informacije o svim transakcijama, kao što su datum i vrijednost.

#### Instant placanje i prenos sredstava
- **US-3:** Kao korisnik, zelim izvršiti instant placanje i prenos sredstava kako bih brzo i lako obavljao financijske transakcije.
	+ **AC-3.1:** Pogledajmo detaljne informacije o svim prenosima sredstava, kao što su datum i vrijednost.
	+ **AC-3.2:** Uključite mogućnost brzeg izvršavanja transakcija.

#### Placanje racuna skeniranjem QR/IPS koda
- **US-5:** Kao korisnik, zelim platiti racunama skeniranjem QR/IPS koda kako bih brzo i lako obavljao financijske transakcije.
	+ **AC-5.1:** Pogledajmo detaljne informacije o svim platnjama racunama, kao što su datum i vrijednost.
	+ **AC-5.2:** Uključite mogućnost brzeg izvršavanja transakcija.

#### Otvaranje stednje
- **US-7:** Kao korisnik, zelim otvoriti stednju kako bih pristupio svim racunima koji su u stednju.
	+ **AC-7.1:** Pogledajmo detaljne informacije o svim stednjima, kao što su datum i opis stednje.
	+ **AC-7.2:** Uključite mogućnost pristupanja racunima koji su u stednju.

#### Blokada kartice
- **US-9:** Kao korisnik, zelim blokirati karticu kako bih zaštitio svije finance.
	+ **AC-9.1:** Pogledajmo detaljne informacije o blokiranoj kartici, kao što su datum i opis razloga.
	+ **AC-9.2:** Uključite mogućnost brzeg izvršavanja transakcija.

#### Podesavanje limita
- **US-11:** Kao korisnik, zelim podesavati limite racuna kako bih kontrolirao svije finance.
	+ **AC-11.1:** Pogledajmo detaljne informacije o svim podesavanima limita, kao što su datum i opis promjene.
	+ **AC-11.2:** Uključite mogućnost brzeg izvršavanja transakcija.

#### Saljivanje push notifikacija o transakcijama
- **US-13:** Kao korisnik, zelim primati push notifikacije o svim transakcijama kako bih bio upozoren za sve finance.
	+ **AC-13.1:** Pogledajmo detaljne informacije o svim notifikacijama, kao što su datum i opis transakcije.
	+ **AC-13.2:** Uključite mogućnost brzeg primanja notifikacija.

### Administrator
#### Saljivanje informacija o korisnicima i transakcijama
- **US-15:** Kao administrator, zelim saljiti informacije o korisnicima i transakcijama kako bih upozorio se za sve finance.
	+ **AC-15.1:** Pogledajmo detaljne informacije o svim korisnicima i transakcijama, kao što su datum i opis aktivnosti.
	+ **AC-15.2:** Uključite mogućnost brzeg saljanja informacija.

#### Saljivanje push notifikacija o transakcijama
- **US-17:** Kao administrator, zelim saljiti push notifikacije o transakcijama kako bih upozorio se za sve finance.
	+ **AC-17.1:** Pogledajmo detaljne informacije o svim notifikacijama, kao što su datum i opis transakcije.
	+ **AC-17.2:** Uključite mogućnost brzeg primanja notifikacija.

#### Kontrola regulativne kontrolne
- **US-19:** Kao administrator, zelim kontrolirati sve finance kako bih siguran da se sreću s regulativnim standardima.
	+ **AC-19.1:** Pogledajmo detaljne informacije o svim kontrolama, kao što su datum i opis aktivnosti.
	+ **AC-19.2:** Uključite mogućnost brzeg izvršavanja transakcija.

## Nefunkcionalni zahtevi

| Kategorija | Zahtev | Merljiva meta |
| --- | --- | --- |
| Korisnik | 1. Brza i laka korist | < 2s |
| Korisnik | 2. Pregled detalja transakcija | Dostupnost >= 99% |
| Korisnik | 3. Uključivanje općih informacija o racunu | Dostupnost >= 95% |
| Korisnik | 4. Brzo izvršavanje transakcija | < 1s |
| Administrator | 5. Saljanje informacija o korisnicima i transakcijama | Dostupnost >= 99% |
| Administrator | 6. Kontrola regulativne kontrolne | Dostupnost >= 95% |
| Korisnik | 7. Uključivanje općih informacija o stednju | Dostupnost >= 90% |
| Korisnik | 8. Brzo izvršavanje transakcija | < 1s |
| Administrator | 9. Saljanje push notifikacija o transakcijama | Dostupnost >= 99% |
| Administrator | 10. Kontrola regulativne kontrolne | Dostupnost >= 95% |

Poznatke:
- Dostupnost: % dostupa korisnika ili administratora.
- < >: vrijednost u sekundima.
- Dostupnost >= x%: % dostopa korisnika ili administratora.
