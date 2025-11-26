## Viikko 3

- Tehtiin ohjelman CLI & yksinkertainen backend
- Tehtiin backendiin hakemistorakenne, niin että src hakemistossa on 
encryption hakemisto, jossa on omat tiedostot salaamiselle, salauksen 
purkamiselle, salausavaimen luontiin (väliaikainen), sekä tests hakemisto,
jossa on tiedosto yksikkötestiä varten
- Tehtiin `index.py` josta löytyy käyttöliittymä
- Testattu että yksinkertainen yksikkötesti sekä invoke toimii 
- Lisättiin myös poetryyn Invoke, cryptography, coverage, pytest 
riippuvuudet
- Lisättiin `README.md` tiedostoon linkki tähän `changelog.md` tiedostoon
- Päivitettiin `tuntikirjanpito.md` tiedostoa

## Viikko 4

- Vaihdettiin avaimen hallinta tiedostopohjaisesta `KeyManager`-luokasta salasanasta johdettuun avaimeen (`get_key_from_password`, PBKDF2 + salt.bin, Fernet).
- Uudistettiin komentorivikäyttöliittymä: salasana kysytään kahdesti ohjelman alussa, lisättiin ohjevalikko sekä automaattinen alkuperäisen/salatun tiedoston poisto salauksen tai purun onnistuessa.
- Lisättiin `introduction.py`-moduuli ja tietoturvaa kuvaava osuus README:hen sekä arkkitehtuurikaavio (`arkkitehtuuri.md` + upotettu PNG).
- Päivitettiin yksikkötestit käyttämään uutta avainlogiikkaa ja encryptor/decryptor-luokkia sekä lisättiin `lint` Invoke-tehtävä pylint tarkistusten ajamiseen.

# Viikko 5

- GUI
- Sovelluksen kaikki tekstit englanniksi