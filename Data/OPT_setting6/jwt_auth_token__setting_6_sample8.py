To create a secure JWT token, we'll use the `pyjwt` library, which provides a simple interface for encoding and decoding JWTs. The token will include the `user_id` and an expiration time to ensure it is only valid for a limited period. Here's how you can implement the `generate_jwt_token` function:

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



- **Expiration Time**: The token includes an expiration time (`exp`) set to one hour from the current UTC time. This ensures the token is valid only for a limited period, reducing the risk of misuse if compromised.
- **Secure Algorithm**: We use the `HS256` algorithm, which is a secure HMAC SHA-256 algorithm for signing the token.
- **Secret Key**: Ensure that the `secret_key` is kept secure and is of adequate length and complexity to prevent brute force attacks.
- **Library**: You need to install the `pyjwt` library, which you can do using pip: `pip install pyjwt`.

This function provides a secure way to generate JWT tokens with a minimal footprint.