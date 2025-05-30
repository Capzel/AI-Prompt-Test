Certainly! Below is a Python function that generates a random password of a specified length, including uppercase letters, lowercase letters, digits, and special characters.

import secrets
import string

def generate_secure_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]
    
    all_characters = lowercase + uppercase + digits + special_characters
    password_chars.extend(secrets.choice(all_characters) for _ in range(length - 4))
    
    secrets.SystemRandom().shuffle(password_chars)
    
    return ''.join(password_chars)

password_length = 12
print(generate_secure_password(password_length))

- **Security**: Uses the `secrets` module for cryptographically secure random choices.
- **Character Variety**: Ensures the password contains at least one character from each required category.
- **Shuffling**: Shuffles the final password to ensure randomness even with predefined starting characters.
- **Error Handling**: Raises an exception if the length is less than 4, as it's necessary to include each character type.