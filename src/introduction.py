HELP_TEXT = """
--- Instructions ---

This program allows you to encrypt and decrypt individual files.

Password:
- The program asks for the password twice at startup.
- All encrypted files are tied to this one password.
- If you forget the password, the files can no longer be opened.

Security:
- The key is derived from the password using the PBKDF2-HMAC-SHA256 function.
- Files are encrypted using the Fernet encryption from the cryptography library.
- An attacker cannot open the files without the correct password,
  even if they see the code and the salt.bin file.

File deletion:
- When encryption succeeds, the original (unencrypted) file is deleted.
- When decryption succeeds, the encrypted file is deleted.

Password choice:
- Use a password that is at least 25 characters long, looks random,
  and that you do not use anywhere else.
"""


def print_help():
    print(HELP_TEXT)
