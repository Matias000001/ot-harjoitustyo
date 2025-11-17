from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt_file(self, input_path, output_path):
        
        try:
            with open(input_path, "rb") as infile:
                data = infile.read()
        except FileNotFoundError:
            print("Virhe: salattavaa tiedostoa ei löytynyt.")
            return False
        except PermissionError:
            print("Virhe: ei oikeuksia lukea salattavaa tiedostoa.")
            return False
        except Exception:
            print("Virhe: tapahtui odottamaton virhe tiedostoa luettaessa.")
            return False

        try:
            encrypted = self.fernet.encrypt(data)
        except Exception:
            print("Virhe: salaus epäonnistui.")
            return False
        
        try:
            with open(output_path, "wb") as outfile:
                outfile.write(encrypted)
        except PermissionError:
            print("Virhe: ei oikeuksia kirjoittaa ulostulotiedostoa.")
            return False
        except Exception:
            print("Virhe: tiedoston tallentamisessa tapahtui virhe.")
            return False

        print("Tiedosto salattu onnistuneesti.")
