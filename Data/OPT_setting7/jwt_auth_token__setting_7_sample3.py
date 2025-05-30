To create a JWT token securely, we'll use the `PyJWT` library, which is a popular choice for handling JWTs in Python. The token will include a payload with the `user_id` and an expiration time. We'll use the `HS256` algorithm for signing the token, which is a secure choice for symmetric key encryption.

Here's the implementation:

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


- **Expiration Time**: The token includes an expiration time to ensure it is only valid for a limited period, reducing the risk of misuse if compromised.
- **HS256 Algorithm**: This is a secure hashing algorithm for signing the token.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.