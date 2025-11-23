HELP_TEXT = """
--- Ohjeet ---

Tällä ohjelmalla voit salata ja purkaa yksittäisiä tiedostoja.

Salasana:
- Ohjelma kysyy salasanan kahdesti käynnistyessä.
- Kaikki salatut tiedostot ovat sidottuja tähän yhteen salasanaan.
- Jos unohdat salasanan, tiedostoja ei voi enää avata.

Tietoturva:
- Avain johdetaan salasanasta PBKDF2-HMAC-SHA256 -funktiolla.
- Tiedostot salataan cryptography-kirjaston Fernet-salauksella.
- Hyökkääjä ei voi avata tiedostoja ilman oikeaa salasanaa,
  vaikka näkisi koodin ja salt.bin-tiedoston.

Tiedostojen poistaminen:
- Kun salaus onnistuu, alkuperäinen (salaamaton) tiedosto poistetaan.
- Kun salauksen purku onnistuu, salattu tiedosto poistetaan.

Salasanan valinta:
- Käytä vähintään 25 merkkistä, satunnaisen näköistä salasanaa,
  jota et käytä missään muualla.
"""


def print_help():
    print(HELP_TEXT)
