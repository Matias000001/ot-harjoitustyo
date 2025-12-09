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

## Viikko 5

- Lisätty graafinen käyttöliittymä Tkinterillä (UI-luokka, `gui_main.py`), jossa salasana annetaan yhdessä ikkunassa ja tiedostot valitaan dialogeilla.
- Toteutettu GUI-versioon tiedostojen salaus ja purku sekä alkuperäisen/salatun tiedoston automaattinen poisto onnistuneen operaation jälkeen.
- Parannettu GUI:n käytettävyyttä: Tab/Enter-navigointi salasanan syöttöön, päävalikon nappeihin ja Ohjeet-näkymän Back-näppiin.
- Säilytetty komentorivikäyttöliittymä (`index.py`) rinnalla ja lisätty `invoke gui`-taski graafisen version käynnistämiseen.
- Päivitetty README vastaamaan uutta rakennetta (CLI + GUI, invoke-komennot, testaus ja linttaus).
- Lisätty uusia yksikkötestejä salausmoduuleille (Encryptor, Decryptor, key_manager) ja nostettu testikattavuus yli kurssin vaatimuksen.
- Päivitetty `.coveragerc` niin, että käyttöliittymä- ja testikoodi rajataan testikattavuusraportin ulkopuolelle kurssiohjeen mukaisesti.
- Lisätty `salt.bin` ja PyInstallerin tuottamat tiedostot (.spec, dist, build) `.gitignore` -tiedostoon ja siivottu repo niiden osalta.
- Rakennettu ensimmäinen itsenäinen binääri (CipherVault) PyInstallerilla ja testattu sen käynnistyminen Linux-ympäristössä.
- Lisätty dokumentaatioon tiedoston salaamista kuvaava sekvenssikaavio ja linkitetty arkkitehtuuri.md README:stä.
- (Kurssivaatimusten ulkopuolella) kokeiltu sovelluksen jakelua erillisinä ajettavina paketteina PyInstallerilla Linuxille ja Windowsille.

## Viikko 6

- Eriytetty selkeämmin sovelluslogiikkaa ja käyttöliittymälogiikkaa eri moduuleihin.
- Kysymys ennen tiedostojen poistoa
- Lisättiin testejä (coverage 71%)
- Lisättiin autopep8-muotoilu invoke-tehtäväksi ja päivitettiin, changelog.md, README.md, tuntikirjanpito.md, tasks.py
- Aloitettu ohjeiden mukaisesti docstring-dokumentointi
- tehtiin vertaisarviointi
- arkkitehtuurikuvaus ja kaavio päivitetty vastaamaan tätä hetkeä
- käyttöohje lisätty
- testiraportista kuva lisätty