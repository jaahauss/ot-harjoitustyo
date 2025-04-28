<h1>Laivanupotus (Battleship)</h1>

## Harjoitustyön kuvaus

Laivanupotus-peli, jossa tarkoituksena upottaa kaikki sovelluksen luomat laivat. Tarkempi kuvaus löytyy vaatimusmäärittelystä.

## Dokumentaatio

- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](./dokumentaatio/kayttoohje.md)

## Asennus

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman voi suorittaa komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
