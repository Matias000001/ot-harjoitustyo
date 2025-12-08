# pylint: disable=duplicate-code
from cryptography.fernet import Fernet, InvalidToken


class Decryptor:
    def __init__(self, key: bytes):
        self.fernet = Fernet(key)

    def decrypt_file(self, input_path: str, output_path: str) -> bool:
        try:
            with open(input_path, "rb") as infile:
                data = infile.read()
        except FileNotFoundError:
            print("Error: file not found.")
            return False
        except PermissionError:
            print("Error: no permissions to read the file.")
            return False
        try:
            decrypted = self.fernet.decrypt(data)
        except InvalidToken:
            print("Error: Invalid key or file is not encrypted with this program.")
            return False
        try:
            with open(output_path, "wb") as outfile:
                outfile.write(decrypted)
        except PermissionError:
            print("Error: no permissions to write to the file.")
            return False
        return True
