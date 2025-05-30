Certainly! Below is a Python function that generates a random password of a specified length, including uppercase letters, lowercase letters, digits, and special characters. This function uses the `secrets` module, which is suitable for cryptographic purposes, ensuring the password is generated securely.

import secrets
import string

def generate_secure_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password_characters = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]

    all_characters = uppercase + lowercase + digits + special_characters
    password_characters.extend(secrets.choice(all_characters) for _ in range(length - 4))

    secrets.SystemRandom().shuffle(password_characters)

    return ''.join(password_characters)

password_length = 12
print(generate_secure_password(password_length))

- **`secrets` Module**: Used for generating cryptographically secure random numbers.
- **Character Sets**: Includes uppercase, lowercase, digits, and special characters.
- **Minimum Length**: The function ensures the password is at least 4 characters long to include all character types.
- **Shuffling**: Ensures the order of characters is unpredictable.