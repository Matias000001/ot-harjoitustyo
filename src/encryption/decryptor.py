from cryptography.fernet import Fernet, InvalidToken

class Decryptor:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def decrypt_file(self, input_path, output_path):
        
        try:
            with open(input_path, "rb") as infile:
                data = infile.read()
        except FileNotFoundError:
            print("Virhe: tiedostoa ei löytynyt.")
            return False
        except PermissionError:
            print("Virhe: ei oikeuksia lukea tiedostoa.")
            return False

        try:
            decrypted = self.fernet.decrypt(data)
        except InvalidToken:
            print("Virhe: väärä avain tai tiedosto ei ole salattu tällä ohjelmalla.")
            return False
        except Exception:
            print("Virhe: tiedoston purussa tapahtui odottamaton virhe.")
            return False

        try:
            with open(output_path, "wb") as outfile:
                outfile.write(decrypted)
        except PermissionError:
            print("Virhe: ei oikeuksia kirjoittaa tiedostoa.")
            return False
        except Exception:
            print("Virhe: tiedoston tallentamisessa tapahtui virhe.")
            return False

        print("Tiedosto purettu onnistuneesti.")
