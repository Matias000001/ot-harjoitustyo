import os


class FileController:
    def encrypt(self, encryptor, input_path: str, output_path: str):
        ok = encryptor.encrypt_file(input_path, output_path)
        if not ok:
            return False, "Encryption failed."
        try:
            os.remove(input_path)
            return True, "File encrypted. Original file deleted."
        except OSError:
            return True, "File encrypted. Warning: failed to delete original file."

    def decrypt(self, decryptor, input_path: str, output_path: str):
        ok = decryptor.decrypt_file(input_path, output_path)
        if not ok:
            return False, "Decryption failed."
        try:
            os.remove(input_path)
            return True, "File decrypted. Encrypted file deleted."
        except OSError:
            return True, "File decrypted. Warning: failed to delete encrypted file."
