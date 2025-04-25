# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on laivanupotuspeli, jossa pelaaja yrittää upottaa laivat mahdollisimman vähillä osumilla.

## Käyttäjät

Vain yksi käyttäjärooli, _pelaaja_ (normaali käyttäjä).

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen ***tehty***
  - Käyttäjätunnuksen täytyy olla uniikki, muuten järjestelmä ilmoittaa tästä ***tehty***
- Käyttäjä voi kirjautua järjestelmään ***tehty***
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle ***tehty***
  - Jos käyttäjätunnus tai salasana ei täsmää, ilmoittaa järjestelmä tästä ***tehty***

### Kirjautumisen jälkeen

- Käyttäjä voi aloittaa uuden pelin ***tehty***
- Sovellus generoi pelilaudan ***tehty***
- Käyttäjä voi liikuttaa kohdistinta pelilaudalla ***tehty***
- Käyttäjä voi tehdä uuden siirron aloitetussa pelissä. ***tehty***
- Käyttäjä näkee oman siirtonsa tuloksen:
  - Osui ***tehty***
  - Osui ja upposi ***tehty***
  - Ohi ***tehty***
- Käyttäjä voi kirjautua ulos näkymästä. ***tehty***

## Jatkokehitysideoita

- Käyttäjä voi itse luoda pelilaudan.
- Vuoropelimahdollisuus:
  - Käyttäjä voi pelata "tekoälyä" vastaan TAI
  - Käyttäjä voi kutsua toisen rekisteröityneen käyttäjän pelaamaan.
- Käyttäjä voi kieltäytyä pelistä/poistaa pelin.
