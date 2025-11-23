from cryptography.fernet import Fernet


class Encryptor:
    def __init__(self, key: bytes):
        self.fernet = Fernet(key)

    def encrypt_file(self, input_path: str, output_path: str) -> bool:
        try:
            with open(input_path, "rb") as infile:
                data = infile.read()
        except FileNotFoundError:
            print("Virhe: salattavaa tiedostoa ei löytynyt.")
            return False
        except PermissionError:
            print("Virhe: ei oikeuksia lukea salattavaa tiedostoa.")
            return False

        encrypted = self.fernet.encrypt(data)

        try:
            with open(output_path, "wb") as outfile:
                outfile.write(encrypted)
        except PermissionError:
            print("Virhe: ei oikeuksia kirjoittaa ulostulotiedostoa.")
            return False

        return True
