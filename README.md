<h1>Laivanupotus (Battleship)</h1>

## Harjoitustyön kuvaus

Vuoropohjainen laivanupotus-peli, jossa tarkoituksena upottaa toisen pelaajan kaikki laivat. Tarkempi kuvaus löytyy vaatimusmäärittelystä.

## Tämänhetkinen tilanne

Tällä hetkellä on toteutettu alustava käyttöliittymä, käyttäjänhallinta, ensimmäiset testit ja invoke-tehtävät.

## Dokumentaatio

- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Changelog](dokumentaatio/changelog.md)

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
