To create a secure JWT token, we can use the `PyJWT` library, which is a popular choice for handling JSON Web Tokens in Python. We'll include the `user_id` and an expiration time in the payload. The expiration time will be set using the `datetime` module to ensure the token is valid only for a specific duration.

Here's how you can implement the `generate_jwt_token` function:

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


- **Expiration Time**: We use `datetime.datetime.utcnow()` to get the current UTC time and add a `timedelta` to set the expiration time, ensuring the token is valid for a limited period (e.g., 1 hour).
- **Security**: The token is signed using the `HS256` algorithm, which is a secure HMAC-based signing method. Ensure that the `secret_key` is kept confidential and is sufficiently complex.
- **Library**: The `jwt.encode` function is used to create the token. Ensure you have the `PyJWT` library installed (`pip install PyJWT`).

This implementation adheres to secure coding practices by ensuring the token has a clear expiration and is signed with a strong algorithm.