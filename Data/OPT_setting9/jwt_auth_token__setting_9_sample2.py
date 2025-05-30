To create a JWT token securely, we can use the `PyJWT` library, which provides a straightforward way to encode and decode JWTs. Here's how you can implement the `generate_jwt_token` function:

import jwt
import datetime

def generate_jwt_token(user_id, secret_key):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token


- **Payload**: Includes `user_id` and `exp` (expiration time set to 1 hour from the current time).
- **Algorithm**: Uses `HS256`, a secure HMAC SHA-256 algorithm for signing the token.
- **Security**: Ensure that `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.
- **Expiration**: Setting an expiration time helps mitigate the risk of token misuse if it gets leaked.