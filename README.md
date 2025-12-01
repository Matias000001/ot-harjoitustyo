# Ohjelmistotekniikka, harjoitustyö

## Cipher Vault - salausohjelma

Sovelluksen käyttäjä pystyy salaamaan ohjelmalla haluamansa tiedostot erittäin turvallisesti. Ohjelma käyttää moderneimpia kryptograafisia menetelmiä, eikä ohjelman  salausta pysty oikein käytettynä murtamaan.


## Tietoturvahuomio käyttäjälle

Tämä ohjelma ei tallenna salausavainta minnekään, vaan avain johdetaan aina sinun antamastasi salasanasta.
Jos unohdat salasanan, kukaan ei pysty avamaan salattuja tiedostoja - ei edes ohjelman tekijä.


### Millainen salasanan pitää olla?

Jotta tiedostosi olisivat turvassa myös valtiollisia toimijoita ja supertietokoneita vastaan:

- Salasanan pituus vähintään **25 merkkiä**
- Käytä **isoja ja pieniä kirjaimia, numeroita ja erikoismerkkejä**
- Älä käytä sanoja, nimiä, päivämääriä tai muuta helposti arvattavaa

### Käytetty salaus

- Avain johdetaan salasanasta funktiolla **PBKDF2-HMAC-SHA256**
- Suola tallennetaan tiedostoon `salt.bin`
- Tiedostot salataan Pythonin **cryptography**-kirjaston **Fernet**-salausta käyttäen
- Sisäisesti tämä käyttää **AES-128-CBC** -salausta sekä **HMAC-SHA256** -allekirjoitusta eheyden tarkistamiseen

**Miksi tämä on turvallista?**

- 25 satunnaisesta merkistä koostuvassa salasanassa on valtava määrä mahdollisia yhdistelmiä.
- Ainoa realistinen hyökkäys on arvata salasanaa brute forcella.
- Ohjelma käyttää PBKDF2-algoritmia, joka hidastaa jokaista arvausta erikseen, joten kaikkien vaihtoehtojen läpikäynti on käytännössä mahdotonta, vaikka hyökkääjällä olisi erittäin tehokas supertietokoneklusteri.
- Mikäli hyökkääjä ei ole asentanut tietokoneellesi keyloggeria eikä salasana ole helposti arvattava, tämä kryptaus on murtamaton.

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testaus.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [GitHub Release](https://github.com/Matias000001/ot-harjoitustyo/releases/tag/viikko5)


## Asennus ja ajaminen

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovelluksen komentorivi versio komennolla:

```bash
poetry run invoke start
```

3. Käynnistä sovelluksen graafinen versio komennolla:

```bash
poetry run invoke gui
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```
```bash
poetry run invoke gui
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

