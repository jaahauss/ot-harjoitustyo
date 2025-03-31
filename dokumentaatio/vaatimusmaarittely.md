# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on laivanupotuspeli, eli vuoropohjainen peli. Kaksi pelaajaa pelaa vuorotellen yrittäen osua toisen pelaajan laivoihin. Voittaja on se, joka on ensin upottanut toisen pelaajan kaikki laivat.

## Käyttäjät

Vain yksi käyttäjärooli, pelaaja eli _normaali käyttäjä_.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle
  - Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä

### Kirjautumisen jälkeen

- Käyttäjä voi aloittaa uuden pelin (pelilauta generoituu automaattisesti)
- Käyttäjä voi kutsua toisen rekisteröityneen käyttäjän pelaamaan.
- Käyttäjä voi tehdä uuden siirron aloitetussa pelissä (jos on hänen vuoronsa).
- Käyttäjä näkee oman siirtonsa tuloksen:
  - Osui
  - Osui ja upposi
  - Ohi
- Käyttäjä näkee toisen pelaajan tekemän siirron.
- Käyttäjä voi kirjautua ulos näkymästä.

## Jatkokehitysideoita

- Käyttäjä voi itse luoda pelilaudan.
- Käyttäjä voi kieltäytyä pelistä/poistaa pelin.
