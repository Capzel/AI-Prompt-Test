Certainly! Below is a Python function that generates a random password with uppercase letters, lowercase letters, digits, and special characters, based on a given length.

import random
import string

def generate_secure_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length must be at least 4")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    if length > 4:
        all_chars = lowercase + uppercase + digits + special_chars
        password_chars.extend(random.choices(all_chars, k=length-4))
    
    random.shuffle(password_chars)

    return ''.join(password_chars)

password_length = 12
password = generate_secure_password(password_length)
print("Generated Password:", password)

- **Character Pools**: We use `string.ascii_lowercase`, `string.ascii_uppercase`, `string.digits`, and `string.punctuation` for different types of characters.
- **Security Measure**: The function ensures the password contains at least one character from each category, enhancing the password's complexity.
- **Shuffling**: The password is shuffled to prevent predictable sequences for the first few characters, which could lead to predictability in partial brute-force attempts.
- **Length Validation**: The minimum length is set to 4 to accommodate at least one of each character type. Adjust accordingly for security requirements.