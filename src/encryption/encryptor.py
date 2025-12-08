from cryptography.fernet import Fernet


class Encryptor:
    def __init__(self, key: bytes):
        self.fernet = Fernet(key)

    def encrypt_file(self, input_path: str, output_path: str) -> bool:
        try:
            with open(input_path, "rb") as infile:
                data = infile.read()
        except FileNotFoundError:
            print("Error: No file to encrypt was found.")
            return False
        except PermissionError:
            print("Error: No permissions to read the file to be encrypted.")
            return False
        encrypted = self.fernet.encrypt(data)
        try:
            with open(output_path, "wb") as outfile:
                outfile.write(encrypted)
        except PermissionError:
            print("Error: no permissions to write output file.")
            return False
        return True
