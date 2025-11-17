import unittest
from encryption.key_manager import KeyManager
from encryption.encryptor import Encryptor
from encryption.decryptor import Decryptor

class TestEncryption(unittest.TestCase):
    def test_encrypt_and_decrypt(self):
        km = KeyManager("test_key.key")
        key = km.generate_key()
        enc = Encryptor(key)
        dec = Decryptor(key)

        original_data = b"Hello world!"
        encrypted = enc.fernet.encrypt(original_data)
        decrypted = dec.fernet.decrypt(encrypted)

        self.assertEqual(decrypted, original_data)