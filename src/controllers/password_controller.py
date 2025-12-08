from encryption.key_manager import get_key_from_password
from encryption.encryptor import Encryptor
from encryption.decryptor import Decryptor


class PasswordController:
    def validate_and_create_engines(self, pw1: str, pw2: str):
        if not pw1:
            return None, None, "Password cannot be empty."
        if pw1 != pw2:
            return None, None, "Passwords do not match."
        key = get_key_from_password(pw1)
        encryptor = Encryptor(key)
        decryptor = Decryptor(key)
        return encryptor, decryptor, None
