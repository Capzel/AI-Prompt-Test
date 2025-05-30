Certainly! Below is a Python function that generates a random password of a given length. This password includes uppercase letters, lowercase letters, digits, and special characters. We use the `random.SystemRandom` class for cryptographically secure random number generation.

import string
import random

def generate_secure_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    all_characters = lowercase + uppercase + digits + special_characters
    password += random.sample(all_characters, length - 4)

    random.SystemRandom().shuffle(password)

    return ''.join(password)

print(generate_secure_password(12))

- **Security**: Utilizes `random.SystemRandom` for secure random number generation.
- **Character Variety**: Ensures at least one character from each category (uppercase, lowercase, digits, special characters) is included.
- **Shuffle**: Final password is shuffled to remove any predictable patterns in character placement.