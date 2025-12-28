from encryption.key_manager import get_key_from_password
from encryption.encryptor import Encryptor
from encryption.decryptor import Decryptor


class PasswordController:
    MIN_LENGTH = 8
    MAX_LENGTH = 128
    
    def validate_and_create_engines(self, pw1: str, pw2: str):
        if not pw1:
            return None, None, "Password cannot be empty."
        if pw1 != pw2:
            return None, None, "Passwords do not match."
        if len(pw1) < self.MIN_LENGTH or len(pw1) > self.MAX_LENGTH:
            return None, None, "Password length must be between {} and {} characters.".format(self.MIN_LENGTH, self.MAX_LENGTH)
        
        key = get_key_from_password(pw1)
        encryptor = Encryptor(key)
        decryptor = Decryptor(key)
        return encryptor, decryptor, None
