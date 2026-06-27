<!-- Test: 3_mobilno_bankarstvo.txt | rezim: registar_rizika | model: llama3.2 | 2026-06-27 12:18 -->

# Procena rizika

## Korak 1 — Kljucne komponente i resursi

### Kljucne komponente i resurse

1. **Baza podataka** - za spremanje korisnickih podataka, transakcija i racuna.
2. **Autentikacija** - sistema za prijavljanje korisnika, kao što je korisnicko ime i lozinka, te biometrijska autentifikacija (otisak prsta/lice) ili jednokratni kod.
3. **API integracija** - za povezivanje sa core banking sistemom banke i slanje push notifikacija o transakcijama.
4. **Finansijski servisi** - za rad sa osetljivim finansijskim podacima, kao što je placanje racuna skeniranjem QR/IPS koda.
5. **Push notifikacije** - za slanje notifikacija korisnicima o transakcijama i drugim relevantnim informacijama.
6. **Regulativna usklađenost** - za usklađivanje aplikacije sa regulativom (NBS, GDPR) i podrška 24/7.
7. **Skeniranje QR/IPS koda** - za placanje racuna skeniranjem QR/IPS koda.
8. **Blokada kartice** - za blokadu korisnickih kartica.
9. **Podesavanje limita** - za podesavanje limita korisnikom.
10. **Instant placanje** - za instant placanje i prenos sredstava.
11. **Pregled stanja i prometa po racunima** - za pregled stanja i prometa po racunima.
12. **Integracija sa core banking sistemom** - za integraciju aplikacije sa core banking sistemom banke.

Izdvojeni resursi:
- Core banking sistem
- Regulativni dokumenti (NBS, GDPR)

## Korak 2 — Identifikovani rizici

### Identifikovani rizici

#### 1. **Baza podataka**
- **R-1:** Nepokvarena integritet podataka u bazi, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih podataka i potrebno izmeniti strukturu baze za spremanje podataka.
- **R-3:** Nepokvarena sigurnosna konfiguracija baze, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 2. **Autentikacija**
- **R-1:** Nepokvarena autentifikacijska metoda, što može dovesti do neprekidanog pristupa korisnickim podacima.
- **R-2:** Brzo rast korisnika i potrebno izmeniti autentifikacijsku konfiguraciju za spremanje korisnickih podataka.
- **R-3:** Nepokvarena sigurnosna konfiguracija autentifikacije, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 3. **API integracija**
- **R-1:** Nepokvarena integritet API-a, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih API-a i potrebno izmeniti API-konfiguraciju za spremanje korisnickih podataka.
- **R-3:** Nepokvarena sigurnosna konfiguracija API-a, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 4. **Finansijski servisi**
- **R-1:** Nepokvarena integritet finansijskih podataka, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih finansijskih podataka i potrebno izmeniti strukturu baze za spremanje podataka.
- **R-3:** Nepokvarena sigurnosna konfiguracija finansijskih podataka, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 5. **Push notifikacije**
- **R-1:** Nepokvarena integritet push notifikacija, što može dovesti do neprekidanog rada aplikacije ili pogrešnih notifikacija.
- **R-2:** Brzo rast korisnickih push notifikacija i potrebno izmeniti konfiguraciju za spremanje notifikacija.
- **R-3:** Nepokvarena sigurnosna konfiguracija push notifikacija, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 6. **Regulativna usklađenost**
- **R-1:** Nepokvarena usklađenost sa regulativom (NBS, GDPR), što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih podataka i potrebno izmeniti strukturu baze za spremanje podataka.
- **R-3:** Nepokvarena sigurnosna konfiguracija aplikacije, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 7. **Skeniranje QR/IPS koda**
- **R-1:** Nepokvarena integritet skenirane informacije, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih QR/IPS koda i potrebno izmeniti konfiguraciju za spremanje skenirane informacije.
- **R-3:** Nepokvarena sigurnosna konfiguracija skeniranja QR/IPS koda, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 8. **Blokada kartice**
- **R-1:** Nepokvarena integritet blokadne informacije, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih kartica i potrebno izmeniti konfiguraciju za spremanje blokadne informacije.
- **R-3:** Nepokvarena sigurnosna konfiguracija blokadne informacije, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 9. **Podesavanje limita**
- **R-1:** Nepokvarena integritet podesavanja limita, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih limita i potrebno izmeniti konfiguraciju za spremanje limita.
- **R-3:** Nepokvarena sigurnosna konfiguracija podesavanja limita, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 10. **Instant placanje**
- **R-1:** Nepokvarena integritet instant plasnenja, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih instant plasenja i potrebno izmeniti konfiguraciju za spremanje instant plasenja.
- **R-3:** Nepokvarena sigurnosna konfiguracija instant plasnenja, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 11. **Pregled stanja i prometa po racunima**
- **R-1:** Nepokvarena integritet pregleda stanja i prometa, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih racuna i potrebno izmeniti konfiguraciju za spremanje pregleda stanja i prometa.
- **R-3:** Nepokvarena sigurnosna konfiguracija pregleda stanja i prometa, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### 12. **Integracija sa core banking sistemom**
- **R-1:** Nepokvarena integritet integracije, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih integracija i potrebno izmeniti konfiguraciju za spremanje integracije.
- **R-3:** Nepokvarena sigurnosna konfiguracija integracije, što može dovesti do neprekidanog pristupa korisnickim podacima.

#### Izdvojeni resursi
- **R-1:** Nepokvarena integritet core banking sistema, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija.
- **R-2:** Brzo rast korisnickih integracija i potrebno izmeniti konfiguraciju za spremanje integracije.
- **R-3:** Nepokvarena sigurnosna konfiguracija core banking sistema, što može dovesti do neprekidanog pristupa korisnickim podacima.

## Korak 3 — Registar rizika i prioriteti

## Registar Rizika

### Identifikovani Rizici

| ID | Rizik | Kategorija | V (Verovatnoca) | U (Uticaj) | Nivo (VxU) | Ocena | Strategija | Mera ublazavanja |
|----|-------|-----------|---|---|-----------|-------|-----------|------------------|
|R-1| Nepokvarena integritet baze podataka u aplikaciji| Baza podataka| 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih podataka i potrebno izmeniti strukturu baze za spremanje podataka| Baza podataka | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija baze, što može dovesti do neprekidanog pristupa korisnickim podacima| Baza podataka | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet autentifikacije u aplikaciji| Autentikacija | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih korisnika i potrebno izmeniti autentifikacijsku konfiguraciju za spremanje korisnickih podataka| Autentikacija | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija autentifikacije, što može dovesti do neprekidanog pristupa korisnickim podacima| Autentikacija | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet API-a, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija| API integracija | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih API-a i potrebno izmeniti API-konfiguraciju za spremanje korisnickih podataka| API integracija | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija API-a, što može dovesti do neprekidanog pristupa korisnickim podacima| API integracija | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet finansijskih podataka, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija| Finansijski servisi | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih finansijskih podataka i potrebno izmeniti strukturu baze za spremanje podataka| Finansijski servisi | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija finansijskih podataka, što može dovesti do neprekidanog pristupa korisnickim podacima| Finansijski servisi | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet push notifikacija, što može dovesti do neprekidanog rada aplikacije ili pogrešnih notifikacija| Push notifikacije | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih push notifikacija i potrebno izmeniti konfiguraciju za spremanje notifikacija| Push notifikacije | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija push notifikacija, što može dovesti do neprekidanog pristupa korisnickim podacima| Push notifikacije | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena usklađenost sa regulativom (NBS, GDPR), što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija| Regulativna usklađenost | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih podataka i potrebno izmeniti strukturu baze za spremanje podataka| Regulativna usklađenost | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija aplikacije, što može dovesti do neprekidanog pristupa korisnickim podacima| Regulativna usklađenost | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet skenirane informacije, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija| Skeniranje QR/IPS koda | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih QR/IPS koda i potrebno izmeniti konfiguraciju za spremanje skenirane informacije| Skeniranje QR/IPS koda | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija skeniranja QR/IPS koda, što može dovesti do neprekidanog pristupa korisnickim podacima| Skeniranje QR/IPS koda | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet autentifikacije u aplikaciji| Autentikacija | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih korisnika i potrebno izmeniti autentifikacijsku konfiguraciju za spremanje korisnickih podataka| Autentikacija | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija autentifikacije, što može dovesti do neprekidanog pristupa korisnickim podacima| Autentikacija | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet API-a, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija| API integracija | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih API-a i potrebno izmeniti API-konfiguraciju za spremanje korisnickih podataka| API integracija | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija API-a, što može dovesti do neprekidanog pristupa korisnickim podacima| API integracija | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet finansijskih podataka, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija| Finansijski servisi | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih finansijskih podataka i potrebno izmeniti strukturu baze za spremanje podataka| Finansijski servisi | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija finansijskih podataka, što može dovesti do neprekidanog pristupa korisnickim podacima| Finansijski servisi | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet push notifikacija, što može dovesti do neprekidanog rada aplikacije ili pogrešnih notifikacija| Push notifikacije | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih push notifikacija i potrebno izmeniti konfiguraciju za spremanje notifikacija| Push notifikacije | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija push notifikacija, što može dovesti do neprekidanog pristupa korisnickim podacima| Push notifikacije | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena usklađenost sa regulativom (NBS, GDPR), što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija| Regulativna usklađenost | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih podataka i potrebno izmeniti strukturu baze za spremanje podataka| Regulativna usklađenost | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija aplikacije, što može dovesti do neprekidanog pristupa korisnickim podacima| Regulativna usklađenost | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-1| Nepokvarena integritet skenirane informacije, što može dovesti do neprekidanog rada aplikacije ili pogrešnih transakcija| Skeniranje QR/IPS koda | 3 | 4 | 12 | Srednji | Izbegavanje / ublazavanje / prenos | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |
|R-2| Brzo rast korisnickih QR/IPS koda i potrebno izmeniti konfiguraciju za spremanje skenirane informacije| Skeniranje QR/IPS koda | 4 | 3 | 12 | Srednji | Izmena konfiguracije baze, obavestivanje korisnika o potrebi za izmenom |
|R-3| Nepokvarena sigurnosna konfiguracija skeniranja QR/IPS koda, što može dovesti do neprekidanog pristupa korisnickim podacima| Skeniranje QR/IPS koda | 5 | 4 | 20 | Visok | Implementacija novih sigurnosnih mehanizama, obavestivanje korisnika o potrebi za izmenom |

### Strategije:

- **Izbegavanje**: Izbegavanje rizika je najbolji način da se sastane sa situacijom bez potrebno uvođenja novih mehanizama ili obavestivanja korisnika.
- **Ublazavanje**: Ublazivanje rizika je proces izmena ili poboljšanja postojećih mehanizama ili konfiguracija za smanjenje rizika.
- **Prenos**: Prenos rizika je proces prenosa zada ili rizika na drugog subjekta ili organizaciju, što može biti potrebno u slučaju kada se ne mogu izvršiti izmena ili poboljšanje postojećih mehanizama.

### Mere ublazavanja:

- **Implementacija novih sigurnosnih mehanizama**: Implementacija novih sigurnosnih mehanizama ili konfiguracija za smanjenje rizika.
- **Obavestivanje korisnika o potrebi za izmenom**: Obavestivanje korisnika o potrebi za izmenom ili poboljšanje postojećih mehanizama.
- **Izmena konfiguracije baze**: Izmena konfiguracije baze ili sistema za spremanje podataka.
- **Obavestivanje korisnika o potrebi za izmenom**: Obavestivanje korisnika o potrebi za izmenom ili poboljšanje postojećih mehanizama.
