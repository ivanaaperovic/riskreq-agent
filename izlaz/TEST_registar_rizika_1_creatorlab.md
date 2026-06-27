<!-- Test: 1_creatorlab.txt | rezim: registar_rizika | model: llama3.2 | 2026-06-27 12:00 -->

# Procena rizika

## Korak 1 — Kljucne komponente i resursi

### Kljucne komponente i resurse

1. **Baza podataka**: MySQL ili druga baza podataka koja podržava WordPress/ WooCommerce integraciju.
2. **Autentikacija i korisnički sustav**: WordPress REST API, WordPress User Model, WordPress Authentication Plugin (npr. WP Auth) za autentikaciju korisnika.
3. **Plaćanje i online plaćanje**: Stripe ili drugi eksterni servis koji podržava online plaćanje.
4. **Sustav za kupovinu**: WooCommerce za integraciju s WordPressom, WooCommerce Cart & Checkout za implementaciju online kupnje.
5. **Servis za hostiranje sadržaja**: Platforma kao što je YouTube ili drugi servis koji podržava hostiranje video lekcija.
6. **E-pošta i email servisi**: Npr. Mailgun ili Sendgrid za slanje emailova potvrde o kupovini.
7. **Podaci o korisnicima**: WordPress User Model, WordPress Custom Post Type (npr. korisnik) za cuvanje podataka o korisnicima.
8. **Integracije i API**: WordPress REST API, WooCommerce API za integraciju s drugim sustavom i eksternim servisima.
9. **Sustav za pristup video lekcijama**: Npr. WordPress Custom Post Type (npr. video lekcija) za cuvanje sadržaja i implementaciju sustava za pristup.
10. **Sustav za administraciju**: WordPress sa administratorulom koji podržava dodavanje kurseva, cene i opisa, kao i pravljenje raporta o prodaji.

## Korak 2 — Identifikovani rizici

### Identifikovani rizici

#### 1. **Baza podataka**
- **R-1:** Nedostaje podrška za MySQL, što može dovesti do problema pri integraciji sa WordPress/ WooCommerce.
- **R-2:** Nepokretna baza podataka može dovesti do brzine i performancije problema.
- **R-3:** Nepokretna baza podataka može biti ugrožena od strane napada na sigurnost.

#### 2. **Autentikacija i korisnički sustav**
- **R-1:** WP Auth nešto nepredvidljivo ili nepovoljno za korisničke potrebe.
- **R-2:** Nepokretni sustavi za autentifikaciju mogu biti ugroženi od strane napada na sigurnost.
- **R-3:** WP REST API nešto nepredvidljivo ili nepovoljno za korisničke potrebe.

#### 3. **Plaćanje i online plaćanje**
- **R-1:** Nepokretni servis za online plaćanje može biti ugrožen od strane napada na sigurnost.
- **R-2:** Nepokretni servis za online plaćanje nešto nepredvidljivo ili nepovoljno za korisničke potrebe.
- **R-3:** Nepokretni servis za online plaćanje može biti ugrožen od strane brzine i performancije problema.

#### 4. **Sustav za kupovinu**
- **R-1:** Nepokretni sustavi za kupovinu mogu biti ugroženi od strane napada na sigurnost.
- **R-2:** Nepokretni sustavi za kupovinu nešto nepredvidljivo ili nepovoljno za korisničke potrebe.
- **R-3:** Nepokretni sustavi za kupovinu mogu biti ugroženi od strane brzine i performancije problema.

#### 5. **Servis za hostiranje sadržaja**
- **R-1:** Nepokretna platforma može biti ugrožena od strane napada na sigurnost.
- **R-2:** Nepokretna platforma nešto nepredvidljivo ili nepovoljno za hostiranje video lekcija.
- **R-3:** Nepokretna platforma može biti ugrožena od strane brzine i performancije problema.

#### 6. **E-pošta i email servisi**
- **R-1:** Nepokretni servisi za slanje emailova mogu biti ugroženi od strane napada na sigurnost.
- **R-2:** Nepokretni servisi za slanje emailova nešto nepredvidljivo ili nepovoljno za korisničke potrebe.
- **R-3:** Nepokretni servisi za slanje emailova mogu biti ugroženi od strane brzine i performancije problema.

#### 7. **Podaci o korisnicima**
- **R-1:** Nedostaje podrška za WordPress User Model, što može dovesti do problema pri cuvanju podataka o korisnicima.
- **R-2:** Nepokretna baza podataka može biti ugrožena od strane napada na sigurnost.
- **R-3:** Nedostaje podrška za WordPress Custom Post Type, što može dovesti do problema pri cuvanju sadržaja o korisnicima.

#### 8. **Integracije i API**
- **R-1:** Nepokretni sustavi za integraciju mogu biti ugroženi od strane napada na sigurnost.
- **R-2:** Nepokretni sustavi za integraciju nešto nepredvidljivo ili nepovoljno za korisničke potrebe.
- **R-3:** Nepokretni sustavi za integraciju mogu biti ugroženi od strane brzine i performancije problema.

#### 9. **Sustav za pristup video lekcijama**
- **R-1:** Nedostaje podrška za WordPress Custom Post Type, što može dovesti do problema pri implementaciji sustava za pristup.
- **R-2:** Nepokretna platforma može biti ugrožena od strane napada na sigurnost.
- **R-3:** Nedostaje podrška za WordPress Custom Post Type, što može dovesti do problema pri implementaciji sustava za pristup.

#### 10. **Sustav za administraciju**
- **R-1:** Nepokretni sustavi za administraciju mogu biti ugroženi od strane napada na sigurnost.
- **R-2:** Nepokretni sustavi za administraciju nešto nepredvidljivo ili nepovoljno za korisničke potrebe.
- **R-3:** Nepokretni sustavi za administraciju mogu biti ugroženi od strane brzine i performancije problema.

## Korak 3 — Registar rizika i prioriteti

## Registar rizika
| ID | Rizik | Kategorija | V (Verovatnoca) | U (Uticaj) | Nivo (VxU) | Ocena | Strategija | Mera ublazavanja |
|----|-------|-----------|---------------|------------|-----------|-------|-----------|------------------|
| 1  | Nedostaje podrška za MySQL | Integracije i API | 3           | 4         | 12       | Visok  | prihvatanje | implementacija novog sustava za integraciju |
| 2  | Nepokretna baza podataka | Baza podataka | 5           | 5         | 25       | Visok  | ublazavanje | implementacija novih tehniki za podršku brzine i performancije |
| 3  | Nepokretni sustavi za autentifikaciju | Autentikacija i korisnički sustav | 4           | 5         | 20       | Visok  | ublazavanje | implementacija novih tehniki za podršku sigurnosti |
| 4  | Nepokretni servis za online plaćanje | Plaćanje i online plaćanje | 3           | 4         | 12       | Srednji | prihvatanje | implementacija novog sustava za online plaćanje |
| 5  | Nepokretni sustavi za kupovinu | Sustav za kupovinu | 4           | 5         | 20       | Visok  | ublazavanje | implementacija novih tehniki za podršku brzine i performancije |
| 6  | Nepokretna platforma | Servis za hostiranje sadržaja | 3           | 4         | 12       | Srednji | prihvatanje | implementacija novog sustava za hostiranje sadržaja |
| 7  | Nepokretni servisi za slanje emailova | E-pošta i email servisi | 2           | 3         | 6        | Nizak | ublazavanje | implementacija novih tehniki za podršku brzine i performancije |
| 8  | Nedostaje podrška za WordPress User Model | Podaci o korisnicima | 4           | 5         | 20       | Visok  | prihvatanje | implementacija novog sustava za cuvanje podataka o korisnicima |
| 9  | Nepokretni sustavi za integraciju | Integracije i API | 3           | 4         | 12       | Srednji | prihvatanje | implementacija novih tehniki za podršku integracije |
| 10 | Nedostaje podrška za WordPress Custom Post Type | Sustav za pristup video lekcijama | 5           | 5         | 25       | Visok  | ublazavanje | implementacija novog sustava za pristup video lekcija |
| 11 | Nepokretni sustavi za administraciju | Sustav za administraciju | 4           | 5         | 20       | Visok  | ublazavanje | implementacija novih tehniki za podršku sigurnosti i performancije |

## Top 3 prioritetna rizika
1. **Nedostaje podrška za MySQL**: Rizik je visok jer može dovesti do problema pri integraciji sa WordPress/ WooCommerce, što je ključni deo sistema.
2. **Nepokretna baza podataka**: Rizik je visok jer može biti ugrožena od strane napada na sigurnost i može dovesti do problema pri brzini i performanciji sistema.
3. **Nedostaje podrška za WordPress Custom Post Type**: Rizik je visok jer može dovesti do problema pri implementaciji sustava za pristup video lekcija, što je ključni deo sistema.

Ovaj registar rizika će biti koristan u procesu identifikacije i procene rizika, kao i u implementaciji mera ublazavanja ili prihvatanja kako bi se smanjila verovatnost da će se dogoditi problema.
