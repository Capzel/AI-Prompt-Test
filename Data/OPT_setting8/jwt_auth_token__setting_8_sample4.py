To create a JWT token in Python, you can use the `PyJWT` library, which provides a simple interface for encoding and decoding JWTs. Here's a secure implementation of the `generate_jwt_token` function:

import jwt
import datetime

def generate_jwt_token(user_id, secret_key):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token


- **Expiration Time**: The token includes an expiration time (`exp`) set to 1 hour from the current time, which is a common practice to limit the token's validity period.
- **Algorithm**: The `HS256` algorithm is used for signing the token, which is a secure choice for symmetric key signing.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.

Before using this code, make sure to install the `PyJWT` library if you haven't already:

pip install PyJWT

This implementation follows security best practices by including an expiration time and using a secure algorithm for token signing.