Certainly! Below is a Python function that generates a random password of a specified length, including uppercase letters, lowercase letters, digits, and special characters. The function uses the `secrets` module, which is designed for generating cryptographically secure random numbers, making it suitable for password generation.

import secrets
import string

def generate_secure_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password_characters = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]

    all_characters = lowercase + uppercase + digits + special_characters
    password_characters.extend(secrets.choice(all_characters) for _ in range(length - 4))

    secrets.SystemRandom().shuffle(password_characters)

    return ''.join(password_characters)

password_length = 12
print(generate_secure_password(password_length))

- **`secrets` Module**: Used for generating cryptographically secure random numbers.
- **Character Sets**: Includes lowercase, uppercase, digits, and special characters.
- **Minimum Length**: Ensures the password is at least 4 characters long to include one of each type.
- **Shuffling**: Ensures the order of characters is random.