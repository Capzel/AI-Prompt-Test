Here's how you can generate a random password in Python that includes uppercase letters, lowercase letters, digits, and special characters, using secure random generation:

import string
import secrets

def generate_secure_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character sets.")

    char_sets = {
        'uppercase': string.ascii_uppercase,
        'lowercase': string.ascii_lowercase,
        'digits': string.digits,
        'special': string.punctuation,
    }

    password_chars = [
        secrets.choice(char_sets['uppercase']),
        secrets.choice(char_sets['lowercase']),
        secrets.choice(char_sets['digits']),
        secrets.choice(char_sets['special'])
    ]

    all_chars = ''.join(char_sets.values())
    remaining_length = length - len(password_chars)
    password_chars.extend(secrets.choice(all_chars) for _ in range(remaining_length))

    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

password_length = 12
print(generate_secure_password(password_length))

- Uses the `secrets` module for generating cryptographically secure random numbers.
- Ensures that the password contains at least one character from each of the character sets: uppercase, lowercase, digits, and special characters.
- Password length is validated to ensure all character types can be used, with a minimum length of 4.
- Characters are shuffled to ensure unpredictability of character ordering.