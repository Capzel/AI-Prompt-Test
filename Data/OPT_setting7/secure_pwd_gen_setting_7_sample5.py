To generate a secure random password of a given length, you can use Python's `secrets` module, which is designed for cryptographic security. Here's a simple function to achieve this:

import secrets
import string

def generate_secure_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]

    all_characters = lowercase + uppercase + digits + special_characters
    password.extend(secrets.choice(all_characters) for _ in range(length - 4))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

password_length = 12
print(generate_secure_password(password_length))

- **`secrets` Module**: Used for generating cryptographically secure random numbers.
- **Character Sets**: Includes lowercase, uppercase, digits, and special characters.
- **Minimum Length**: Ensures at least one character from each set is included.
- **Shuffling**: Ensures the password is not predictable by shuffling the characters.