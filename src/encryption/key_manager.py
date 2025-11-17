from cryptography.fernet import Fernet

class KeyManager:
    def __init__(self, path="key.key"):
        self.path = path

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.path, "wb") as f:
            f.write(key)
        return key

    def load_key(self):
        with open(self.path, "rb") as f:
            return f.read()
