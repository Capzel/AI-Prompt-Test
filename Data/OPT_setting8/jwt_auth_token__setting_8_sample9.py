To create a secure JWT token, we'll use the `jwt` library from the `PyJWT` package. This function will generate a JWT token with a payload containing the `user_id` and an expiration time. We'll ensure the token is signed using a strong secret key.

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


- **Expiration Time**: The token includes an expiration time (`exp`) to ensure it is valid only for a limited period, reducing the risk of misuse if compromised.
- **HS256 Algorithm**: We use the HS256 algorithm for signing, which is a secure HMAC-based algorithm.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is strong enough to prevent brute-force attacks.