## Cipher Vault

### Käyttöohje

1. Käynnistys

Komentoriviversio:

```bash
poetry run invoke start
```

Graafinen versio:

```bash
poetry run invoke gui
```

Sovellus kysyy heti alussa salasanan kaksi kertaa. Käytä vahvaa salasanaa, eläkä hukkaa salasanaa, koska salattuja
tiedostoja ei voi muuten palauttaa mitenkään.

2. Käyttöliittymä

Valitse haluatko salata tiedoston (encrypt), avata salatun tiedoston (decrypt), nähdä ohjeet (Help) tai lopettaa ohjelman (quit).

(i) Encrypt file
    1. Valitse salattava tiedosto.
    2. Valitse tallennuspaikka ja nimi salatulle tiedostolle.
    3. Valitse haluatko poistaa salaamattoman version tiedostosta.
    4. Ohjelma ilmoittaa salauksen onnistumisesta.
    5. Tiedosto on salattu.

(ii) Decrypt file
    1. Valitse salatun tiedoston.
    2. Valitse tallennuspaikka ja nimi avattulle tiedostolle.
    3. Valitse haluatko poistaa salatun version tiedostosta.
    4. Ohjelma ilmoittaa purkan onnistumisesta.
    5. Tiedosto on avattu.

(iii) Help
    1. Ohjelma näyttää käyttöohjeen.

(iv) Quit
    1. Ohjelma lopetetaan.