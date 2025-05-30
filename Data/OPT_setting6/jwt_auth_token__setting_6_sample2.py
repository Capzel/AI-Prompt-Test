To create a JWT token securely, we should use the `pyjwt` library, which is designed for encoding and decoding JSON Web Tokens. The function `generate_jwt_token` will include the `user_id` and an expiration time in the payload. We'll utilize the `HS256` algorithm for signing the token. Don't forget to install the library using `pip install pyjwt` if you haven't already.

Here's a secure implementation of the function:

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

- **Expiration Time**: We set an expiration time to ensure the token is only valid for a limited period (e.g., 1 hour).
- **Algorithm**: We use the `HS256` algorithm, which is a widely accepted secure hash algorithm for JWTs.
- **Security Consideration**: Always keep your `secret_key` confidential and ensure it is sufficiently complex to prevent brute force attacks.
- **UTC Time**: The use of `datetime.datetime.utcnow()` ensures consistency in expiration time handling across different time zones.