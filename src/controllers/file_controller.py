import os
from tkinter import messagebox


class FileController:
    """Handles high-level file encryption and decryption operations."""

    def encrypt(self, encryptor, input_path: str, output_path: str):
        """Encrypts a file and optionally deletes the original.

        Args:
            encryptor: Encryptor used for encryption.
            input_path (str): Path to source file.
            output_path (str): Path to encrypted output.

        Returns:
            tuple: (bool success, str message)
        """
        ok = encryptor.encrypt_file(input_path, output_path)
        if not ok:
            return False, "Encryption failed."
        confirm = messagebox.askyesno(
            "Confirm deletion",
            f"Delete original file?\n\n{input_path}"
        )
        if confirm:
            try:
                os.remove(input_path)
                return True, "File encrypted. Original file deleted."
            except OSError:
                return True, "File encrypted. Warning: failed to delete original file."
        else:
            return True, "File encrypted. Original file kept."

    def decrypt(self, decryptor, input_path: str, output_path: str):
        """Decrypts a file and optionally deletes the encrypted source.

        Args:
            decryptor: Decryptor used for decryption.
            input_path (str): Path to encrypted file.
            output_path (str): Path to decrypted output.

        Returns:
            tuple: (bool success, str message)
        """
        ok = decryptor.decrypt_file(input_path, output_path)
        if not ok:
            return False, "Decryption failed."
        confirm = messagebox.askyesno(
            "Confirm deletion",
            f"Delete encrypted file?\n\n{input_path}"
        )
        if confirm:
            try:
                os.remove(input_path)
                return True, "File decrypted. Encrypted file deleted."
            except OSError:
                return True, "File decrypted. Warning: failed to delete encrypted file."
        else:
            return True, "File decrypted. Encrypted file kept."
