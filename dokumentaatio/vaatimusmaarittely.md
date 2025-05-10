# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on laivanupotuspeli, jossa pelaaja yrittää upottaa laivat mahdollisimman vähillä osumilla.

## Käyttäjät

Vain yksi käyttäjärooli, _pelaaja_ (normaali käyttäjä).

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki, muuten järjestelmä ilmoittaa tästä 
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle
  - Jos käyttäjätunnus tai salasana ei täsmää, ilmoittaa järjestelmä tästä

### Kirjautumisen jälkeen

- Käyttäjä voi aloittaa uuden pelin
- Sovellus generoi pelilaudan
- Käyttäjä voi liikuttaa kohdistinta pelilaudalla
- Käyttäjä voi tehdä uuden siirron aloitetussa pelissä.
- Käyttäjä näkee oman siirtonsa tuloksen:
  - Osui
  - Osui ja upposi
  - Ohi
- Käyttäjä voi lopettaa pelin
- Käyttäjä voi kirjautua ulos näkymästä.

## Jatkokehitysideoita

- Käyttäjä voi itse luoda pelilaudan.
- Vuoropelimahdollisuus:
  - Käyttäjä voi pelata "tekoälyä" vastaan TAI
  - Käyttäjä voi kutsua toisen rekisteröityneen käyttäjän pelaamaan.
- Sovellus tallentaa käyttäjän parhaan tuloksen.
