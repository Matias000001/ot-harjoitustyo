# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi salata ja purkaa tiedostoja (esimerkiksi teksti-, kuva- tai muita tiedostoja) vahvalla salauksella niin, että tiedostoja ei voi avata ilman oikeaa salasanaa.  -"tehty"- 
Tarkoituksena on tarjota yksityiskäyttöön turvallinen ja helppokäyttöinen ratkaisu tiedostojen suojaamiseen paikallisesti ilman pilvipalveluja. Sovellus käyttää vahvoja, moderneja salausmenetelmiä ja toimii täysin ilman internetyhteyttä. -"tehty"-

## Käyttäjät

Sovelluksessa on vain yksi käyttäjärooli, normaali käyttäjä. -"tehty"-
Käyttäjällä ei ole tunnuksia eikä rekisteröintiä — kaikki tiedostot suojataan yhdellä salasanalla, joka toimii ainoana suojana tietojen avaamiseen. -"tehty"-
Jos salasana unohtuu, tiedostoja ei voi enää palauttaa. -"tehty"-

## Käyttöliittymäluonnos

Sovellus toimii aluksi teksikäyttöliittymänä (CLI) -"tehty"- ja myöhemmin toteutetaan graafinen käyttöliittymä (GUI). -tehty-

Näkymään aukeaa valikko, joiden takaa löytyy salasanan asettamisen jälkeen toiminnallisuudet:

1. Encrypt file
2. Decrypt file
3. Help
4. Quit

## Ohjelman tarjoamat toiminnallisuudet

### Käynnistyksen jälkeen
- Käyttäjä antaa salasanan kaksi kertaa -"tehty"-
- Käyttäjä näkee valikon (Salaa tiedosto / Pura tiedosto / Ohjeet / Lopeta). -"tehty"-

### Kryptaus
- Ohjelma:
- Lukee tiedoston binäärimuodossa -"tehty"-
- Johdattaa salasanasta salausavaimen -"tehty"-
- Salaa sisällön -"tehty"-
- Tallentaa uuden kryptatun tiedoston käyttäjän antamalla nimellä haluaansa sijaintiin -"tehty"-
- Ohjelma ilmoittaa onnistumisesta tai virheestä (esim. tiedostoa ei löydy). -"tehty"-
- Onnistuessaan poistaa salaamattoman tiedoston. -"tehty"-

### Dekryptaus
- Lukee tiedoston -"tehty"-
- Johdattaa avaimen annetusta salasanasta -"tehty"-
- Purkaa sisällön -"tehty"-
- Jos purku onnistuu, tallentaa alkuperäisen tiedoston käyttäjän antamalla nimellä haluaamaansa sijaintiin -"tehty"-
- Onnistuessaan poistaa salatun tiedoston -"tehty"-

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää voidaan laajentaa esim. seuraavilla ominaisuuksilla:
- Useiden tiedostojen yhtäaikainen salaus (kansio-käsittely)
- Tiedostojen tuhoaminen turvallisesti (secure delete)
- GUI -tehty-
- Sovelluksessa liikkuminen Tab ja Enter nappien avulla -Tehty-
- Kysymys ennen tiedostojen poistoa -Tehty-
