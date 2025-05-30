To securely generate a JWT token with a user ID and an expiration time, you'll want to use the `jwt` library, which is part of the `PyJWT` package. This function will create a JWT with a specific algorithm, typically "HS256", and encode it with a secret key. The expiration time `exp` is often set to a few hours in the future to limit the token's validity.

Here's how you can implement `generate_jwt_token`:

import jwt
import datetime

def generate_jwt_token(user_id, secret_key):
    try:
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # expires in 1 hour
        }
        
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        
        if isinstance(token, bytes):
            token = token.decode('utf-8')
        
        return token
    except Exception as e:
        raise RuntimeError("Error encoding JWT token") from e

- **jwt**: This library provides JSON Web Token encoding and decoding functions.
- **datetime**: Used to handle time operations safely.
- **payload**: Contains `user_id` for identity and `exp` for expiration.
- **algorithm='HS256'**: A secure standard for token signing.
- **Error Handling**: It ensures that any issues during token creation are captured and reported.

To utilize this function securely:
- Ensure `secret_key` remains confidential and is sufficiently long (minimum 256 bits is suggested).
- Regularly rotate `secret_key` following best practices to limit exposure.
- Adjust the token's expiration (`exp`) according to your security needs (shorter is generally safer).