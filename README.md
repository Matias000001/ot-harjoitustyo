# Ohjelmistotekniikka, harjoitustyö

Anomaattori Salausohjelma

Sovelluksen käyttäjä pystyy salaamaan ohjelmalla haluamansa tiedoston. Tällä hetkellä käyttäjä ei vielä pysty lisäämään omaa salasanaa ohjelmalle, vaan
ohjelman key_manager.py genereroi tiedostolle salausavaimen käyttäen cryptographic kirjaston Fernet luokkaa. Myöhemmässä vaiheessa salaus toteutetaan niin, että käyttäjä antaa itse salasanan salaamalleentiedostolle. Salauksen tason tarkoitus on olla silloin niin korkea, että vaikka hyökkääjä pääsisi tutkimaan ohjelman koodia niin tiedostoa ei pystyisi avaamaan ilman tätä salasanaa.

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testaus.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

  ## Asennus (kopioitu referenssisovelluksesta)

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

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