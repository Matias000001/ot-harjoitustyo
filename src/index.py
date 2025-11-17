from encryption.key_manager import KeyManager
from encryption.encryptor import Encryptor
from encryption.decryptor import Decryptor

def main():
    km = KeyManager()

    while True:
        print("\n--- Anomaattori Salausohjelma ---")
        print("1) Generoi avain")
        print("2) Salaa tiedosto")
        print("3) Pura tiedosto")
        print("4) Lopeta")

        valinta = input("Valinta: ").strip()

        if valinta == "1":
            km.generate_key()
            print("Avain generoitu.")

        elif valinta == "2":
            key = km.load_key()
            enc = Encryptor(key)
            inp = input("Anna salattava tiedosto: ").strip()
            out = input("Anna ulostulotiedosto: ").strip()
            ok = enc.encrypt_file(inp, out)
            if ok:
                print("Tiedosto salattu.")

        elif valinta == "3":
            key = km.load_key()
            dec = Decryptor(key)
            inp = input("Anna purettava tiedosto: ").strip()
            out = input("Anna ulostulotiedosto: ").strip()
            ok = dec.decrypt_file(inp, out)
            if ok:
                print("Tiedosto purettu.")

        elif valinta == "4":
            print("Ohjelma suljetaan.")
            break

        else:
            print("Tuntematon valinta.")

if __name__ == "__main__":
    main()
