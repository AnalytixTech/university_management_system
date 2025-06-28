import re

class InvalidEmailError(ValueError):
    """Raised when an email address is not valid."""
    pass


def validate_email(email: str):
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    if not re.match(pattern, email):
        raise InvalidEmailError(f"Invalid email address: {email}")