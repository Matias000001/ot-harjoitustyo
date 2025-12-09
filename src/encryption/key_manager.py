import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

SALT_FILE = "salt.bin"


def _load_or_create_salt() -> bytes:
    """Load an existing salt or create a new one if none exists.

    Returns:
        bytes: The salt used for key derivation.
    """
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            return f.read()
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
        f.write(salt)
    return salt


def get_key_from_password(password: str) -> bytes:
    """Derive a secure encryption key from the given password.

    Args:
        password (str): The user-provided password.

    Returns:
        bytes: A URL-safe base64-encoded encryption key.
    """
    salt = _load_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390_000,
    )
    raw_key = kdf.derive(password.encode("utf-8"))
    return base64.urlsafe_b64encode(raw_key)
