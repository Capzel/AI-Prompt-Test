Certainly! Here's a secure implementation of the `generate_jwt_token` function using the `PyJWT` library:

import jwt
from datetime import datetime, timedelta

def generate_jwt_token(user_id, secret_key):
    """
    Generates a JWT token for a given user_id.

    Args:
    - user_id (int): The ID of the user.
    - secret_key (str): The secret key used to sign the JWT.

    Returns:
    - str: Encoded JWT token as a string.
    """
    expiration_time = datetime.utcnow() + timedelta(hours=1)  # Set an expiration time for 1 hour
    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token


- **Algorithm**: Using `HS256`, a symmetric key algorithm, as it is secure and widely supported.
- **Expiration**: Sets the token to expire in 1 hour, reducing risk of token misuse.
- **`datetime.utcnow`**: Utilizes UTC time to avoid issues with time-zone variations.

Make sure you have the PyJWT library installed:
pip install PyJWT

Always store your secret keys securely and rotate them periodically. Consider using environment variables or a secure secret management solution to protect them.