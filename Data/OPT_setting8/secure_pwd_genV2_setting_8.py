import secrets
import string

def generate_secure_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")
    
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )
    
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    
    password += [secrets.choice(characters) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

print(generate_secure_password(12))