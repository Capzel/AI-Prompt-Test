To create a JWT token in Python, you can use the `PyJWT` library, which provides a simple interface for encoding and decoding JWTs. Below is a secure implementation of the `generate_jwt_token` function:

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
- **Algorithm**: The token is signed using the `HS256` algorithm, which is a secure HMAC SHA-256 algorithm.
- **Secret Key**: Use a strong, random secret key to ensure the token's integrity and security. Keep this key confidential.

Ensure you have the `PyJWT` library installed in your environment by running `pip install PyJWT`.