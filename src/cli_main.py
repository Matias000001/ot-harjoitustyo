from getpass import getpass
from encryption.key_manager import get_key_from_password
from encryption.encryptor import Encryptor
from encryption.decryptor import Decryptor
from introduction import print_help
from controllers.file_controller import FileController

file_controller = FileController()


def print_menu():
    """Print the CLI menu."""
    print("\n--- CipherVault ---")
    print("1) Encrypt file")
    print("2) Extract file")
    print("3) Help")
    print("4) Quit")

def handle_encrypt(encryptor: Encryptor):
    """Encrypt a file via CLI using the given encryptor.

    Args:
        encryptor (Encryptor): Engine used to encrypt the file.
    """

    inp = input("Enter the file to encrypt: ").strip()
    out = input("Enter the output file: ").strip()
    _, msg = file_controller.encrypt(encryptor, inp, out)
    print(msg)

def handle_decrypt(decryptor: Decryptor):
    """Decrypt a file using the CLI interface.

    Args:
        decryptor (Decryptor): Engine used to decrypt the file.
    """
    inp = input("Enter the file to extract: ").strip()
    out = input("Enter the output file: ").strip()
    _, msg = file_controller.decrypt(decryptor, inp, out)
    print(msg)

def ask_password_twice():
    """Ask the user for a password twice and return it.

    Returns:
        str: The confirmed password entered by the user.
    """
    while True:
        pw1 = getpass("Password: ")
        pw2 = getpass("Repeat password: ")
        if not pw1:
            print("Password cannot be empty.")
            continue
        if pw1 != pw2:
            print("Error: passwords do not match. Try again.\n")
            continue
        return pw1

def main():
    """Run the CipherVault CLI application."""
    password = ask_password_twice()
    key = get_key_from_password(password)
    encryptor = Encryptor(key)
    decryptor = Decryptor(key)
    while True:
        print_menu()
        choices = input("Choice: ").strip()
        if choices == "1":
            handle_encrypt(encryptor)
        elif choices == "2":
            handle_decrypt(decryptor)
        elif choices == "3":
            print_help()
        elif choices == "4":
            print("The program is closed.")
            break
        else:
            print("Unknown choice.")

if __name__ == "__main__":
    main()
