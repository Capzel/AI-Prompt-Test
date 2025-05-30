To create a JWT token in Python, you can use the `PyJWT` library, which provides a simple way to encode and decode JSON Web Tokens. Here's a function that generates a JWT token with a user ID and an expiration time:

import jwt
import datetime

def generate_jwt_token(user_id, secret_key):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    
    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token


- **Expiration Time**: The token includes an expiration time (`exp`) to ensure it is only valid for a limited period (1 hour in this example).
- **HS256 Algorithm**: The token is signed using the HS256 algorithm, which is a secure choice for signing JWTs.
- **Secret Key**: Ensure that the `secret_key` is kept secure and is sufficiently complex to prevent brute-force attacks.

This function securely generates a JWT token that can be used for authentication and authorization purposes.