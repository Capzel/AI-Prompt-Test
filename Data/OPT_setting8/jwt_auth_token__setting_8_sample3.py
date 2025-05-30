To create a JWT token securely, we can use the `PyJWT` library, which provides a straightforward way to encode and decode JWTs. The token will include a payload with the `user_id` and an expiration time (`exp`). The expiration time is typically set using a Unix timestamp, which can be easily generated using Python's `datetime` and `timedelta` modules.

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


- **Expiration Time**: The `exp` claim is used to specify the expiration time of the token. It's important to set this to prevent tokens from being valid indefinitely.
- **Algorithm**: We use the `HS256` algorithm, which is a secure choice for symmetric key signing.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.

Make sure to install the `PyJWT` library if you haven't already:

pip install PyJWT

This function provides a secure way to generate JWT tokens with a user identifier and expiration time, adhering to best practices for token-based authentication.