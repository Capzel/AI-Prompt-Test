import random
import string

def generate_secure_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")
    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    password.extend(random.choice(chars) for _ in range(length - 4))
    random.shuffle(password)
    
    return ''.join(password)

print(generate_secure_password())