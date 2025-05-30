To generate a JWT token in Python, you can use the `pyjwt` library, which provides a straightforward way to create and encode JWTs. Below is a secure implementation of the `generate_jwt_token` function. This function includes the user's ID in the payload, along with an expiration time. It uses the `HS256` algorithm for signing the token, which is a secure choice for symmetric key signing.

First, ensure you have the `pyjwt` library installed:

pip install PyJWT

Now, here is the implementation of the `generate_jwt_token` function:

import jwt
from datetime import datetime, timedelta

def generate_jwt_token(user_id, secret_key):
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    
    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token


- **Expiration Time**: The token is set to expire 1 hour from the time of creation. Adjust the `timedelta` as needed.
- **Algorithm**: Uses `HS256`, a secure HMAC SHA-256 signing.
- **Security**: Always keep your `secret_key` safe and never hard-code it in your codebase. Consider using environment variables or a secure vault.
- **Payload**: Includes `user_id` and `exp` (expiration time) which are common requirements for secure tokens.

By following these practices, you ensure that the JWTs are secure and adhere to common security standards.