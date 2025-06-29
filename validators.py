import re
import hashlib

class InvalidEmailError(ValueError):
    pass

class AuthenticationError(ValueError):
    pass


def validate_email(email: str):
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    if not re.match(pattern, email):
        raise InvalidEmailError(f"Invalid email address: {email}")


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed