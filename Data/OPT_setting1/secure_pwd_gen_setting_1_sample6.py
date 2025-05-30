Here's a Python function that securely generates a random password of a specified length, ensuring it includes uppercase letters, lowercase letters, digits, and special characters:

import secrets
import string

def generate_secure_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length must be at least 4 for complexity requirements.")

    character_sets = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation,
    ]
    
    password = [
        secrets.choice(character_set) for character_set in character_sets
    ]
    
    all_characters = ''.join(character_sets)
    password.extend(secrets.choice(all_characters) for _ in range(length - 4))
    
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)


- **`secrets` module**: Used for securely generating random tokens and strings, suitable for cryptographic use.
- **Password Complexity**: Includes at least one of each character type for robust security.
- **Parameter Validation**: Ensures that the requested password length is at least 4 characters, which is the minimum to include one of each character.