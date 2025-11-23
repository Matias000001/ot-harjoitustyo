import os
from getpass import getpass

from encryption.key_manager import get_key_from_password
from encryption.encryptor import Encryptor
from encryption.decryptor import Decryptor
from introduction import print_help


def print_menu():
    print("\n--- Anomaattori Salausohjelma ---")
    print("1) Salaa tiedosto")
    print("2) Pura tiedosto")
    print("3) Ohjeet")
    print("4) Lopeta")


def handle_encrypt(encryptor: Encryptor) -> None:
    inp = input("Anna salattava tiedosto: ").strip()
    out = input("Anna ulostulotiedosto: ").strip()
    ok = encryptor.encrypt_file(inp, out)
    if ok:
        print("Tiedosto salattu.")
        try:
            os.remove(inp)
            print("Alkuperäinen (salaamaton) tiedosto poistettu.")
        except OSError:
            print("Varoitus: alkuperäisen tiedoston poistaminen epäonnistui.")


def handle_decrypt(decryptor: Decryptor) -> None:
    inp = input("Anna purettava tiedosto: ").strip()
    out = input("Anna ulostulotiedosto: ").strip()
    ok = decryptor.decrypt_file(inp, out)
    if ok:
        print("Tiedosto purettu.")
        try:
            os.remove(inp)
            print("Salattu tiedosto poistettu.")
        except OSError:
            print("Varoitus: salatun tiedoston poistaminen epäonnistui.")


def ask_password_twice() -> str:
    while True:
        pw1 = getpass("Anna salasana: ")
        pw2 = getpass("Toista salasana: ")

        if not pw1:
            print("Salasana ei voi olla tyhjä.")
            continue

        if pw1 != pw2:
            print("Virhe: annetut salasanat eivät olleet samat. Yritä uudelleen.\n")
            continue

        return pw1


def main():
    password = ask_password_twice()
    key = get_key_from_password(password)

    encryptor = Encryptor(key)
    decryptor = Decryptor(key)

    while True:
        print_menu()
        valinta = input("Valinta: ").strip()

        if valinta == "1":
            handle_encrypt(encryptor)
        elif valinta == "2":
            handle_decrypt(decryptor)
        elif valinta == "3":
            print_help()
        elif valinta == "4":
            print("Ohjelma suljetaan.")
            break
        else:
            print("Tuntematon valinta.")


if __name__ == "__main__":
    main()
