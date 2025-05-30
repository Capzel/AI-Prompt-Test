To create a secure JWT token, we can use the `PyJWT` library, which provides a straightforward way to encode and decode JWTs. Here's how you can implement the `generate_jwt_token` function:

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
- **Algorithm**: We use the `HS256` algorithm, which is a secure choice for signing JWTs with a secret key.
- **Security**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.