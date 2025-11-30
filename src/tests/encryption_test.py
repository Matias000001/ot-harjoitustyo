import os
import unittest

from encryption.key_manager import get_key_from_password
from encryption.encryptor import Encryptor
from encryption.decryptor import Decryptor


class TestEncryption(unittest.TestCase):
    def setUp(self):
        password = "testi-testi-testi-testi"
        key = get_key_from_password(password)
        self.encryptor = Encryptor(key)
        self.decryptor = Decryptor(key)

    def test_passwords(self):
        password = "salanatestisalasana"
        key1 = get_key_from_password(password)
        key2 = get_key_from_password(password)
        self.assertEqual(key1, key2)

    def test_encrypt_and_decrypt_memory(self):
        original_data = b"Testi-data-testi-data-dii-daa-doo!"
        encrypted = self.encryptor.fernet.encrypt(original_data)
        decrypted = self.decryptor.fernet.decrypt(encrypted)
        self.assertEqual(decrypted, original_data)

    def test_decrypt_file_missing_input_returns_false(self):
        ok = self.decryptor.decrypt_file("tama_on_testi_data_file.enc", "tama_on_toinen_testi_data_file.txt")
        self.assertFalse(ok)
