To create a JWT token securely, we'll use the `PyJWT` library, which is a popular choice for handling JWTs in Python. The token will include a payload with the `user_id` and an expiration time. Here's how you can implement the `generate_jwt_token` function:

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


- **Expiration Time**: The token includes an expiration time (`exp`) to ensure it is only valid for a limited period, reducing the risk of misuse if compromised.
- **Algorithm**: We use the `HS256` algorithm, which is a secure choice for symmetric key signing.
- **Secret Key**: Ensure the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.
- **Library**: `PyJWT` is used for encoding the JWT, which handles the necessary cryptographic operations securely.

Make sure to install the `PyJWT` library if you haven't already:

pip install PyJWT

This function is designed to be secure and maintainable, following best practices for handling JWTs in Python.