# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on laivanupotuspeli, eli vuoropohjainen peli, jossa pelaaja ja vastustaja yrittävät vuorotellen osua toistensa laivoihin. Voittaja on se, joka on ensin upottanut toisen pelaajan kaikki laivat.

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
- Sovellus generoi pelilaudan
- Käyttäjä voi tehdä uuden siirron aloitetussa pelissä (jos on hänen vuoronsa).
- Käyttäjä näkee oman siirtonsa tuloksen:
  - Osui
  - Osui ja upposi
  - Ohi
- Käyttäjä näkee _vastustajan_ tekemän siirron.
- Käyttäjä voi kirjautua ulos näkymästä. ***tehty***

## Jatkokehitysideoita

- Käyttäjä voi itse luoda pelilaudan.
- Käyttäjä voi kutsua toisen rekisteröityneen käyttäjän pelaamaan.
- Käyttäjä voi kieltäytyä pelistä/poistaa pelin.
