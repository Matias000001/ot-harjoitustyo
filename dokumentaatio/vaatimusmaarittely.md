# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi salata ja purkaa tiedostoja (esimerkiksi teksti-, kuva- tai muita tiedostoja) vahvalla salauksella niin, että tiedostoja ei voi avata ilman oikeaa salasanaa.
Tarkoituksena on tarjota yksityiskäyttöön turvallinen ja helppokäyttöinen ratkaisu tiedostojen suojaamiseen paikallisesti ilman pilvipalveluja. Sovellus käyttää vahvoja, moderneja salausmenetelmiä (Argon2id ja ChaCha20-Poly1305) ja toimii täysin ilman internetyhteyttä.

## Käyttäjät

Sovelluksessa on vain yksi käyttäjärooli, normaali käyttäjä.
Käyttäjällä ei ole tunnuksia eikä rekisteröintiä — kaikki tiedostot suojataan yhdellä salasanalla, joka toimii ainoana suojana tietojen avaamiseen.
Jos salasana unohtuu, tiedostoja ei voi enää palauttaa.

## Käyttöliittymäluonnos

Sovellus toimii aluksi teksikäyttöliittymänä (CLI) ja myöhemmin toteutetaan graafinen käyttöliittymä (GUI).

Näkymään aukeaa valikko, joiden takaa löytyy toiminnallisuudet:

1. Encrypt file
2. Decrypt file
3. Exit

## Ohjelman tarjoamat toiminnallisuudet

### Käynnistyksen jälkeen
- Käyttäjä näkee valikon (Encrypt / Decrypt / Exit).
- Käyttäjä voi valita kryptauksen tai dekryptauksen tai ohjelmasta poistumisen.

### Kryptaus
- Käyttäjä antaa:
 - tiedoston absoluuttisen polun (esim. /home/kayttaja/private/kuvat/example.jpg)
 - salasanan kaksi kertaa
- Ohjelma:
 - lukee tiedoston binäärimuodossa
 - johdattaa salasanasta salausavaimen (Argon2id)
 - salaa sisällön (ChaCha20-Poly1305)
 - tallentaa uuden tiedoston, esim. example.enc
- Ohjelma ilmoittaa onnistumisesta tai virheestä (esim. tiedostoa ei löydy).

### Dekryptaus
- Käyttäjä antaa:
 - salatun tiedoston absoluuttisen polun (esim. /home/kayttaja/private/kuvat/example.enc)
 - salasanan
- Ohjelma:
 - lukee tiedoston
 - johdattaa avaimen annetusta salasanasta
 - purkaa sisällön
 - jos salasana on väärä, ilmoittaa virheestä eikä luo tiedostoa
 - jos purku onnistuu, tallentaa alkuperäisen tiedoston (example_decrypted.jpg)

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää voidaan laajentaa seuraavilla ominaisuuksilla:
- Useiden tiedostojen yhtäaikainen salaus (kansio-käsittely)
- Tiedostonimien ja metadatan salaaminen
-  “Vault mode”: hakemisto, jossa kaikki tiedostot salataan automaattisesti
- Tiedostojen tuhoaminen turvallisesti (secure delete)
