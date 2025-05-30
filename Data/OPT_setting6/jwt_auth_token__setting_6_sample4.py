To securely generate a JWT token, we can use the `PyJWT` library, which provides robust functionalities for handling JSON Web Tokens. The following function, `generate_jwt_token`, creates a JWT token with a payload that includes a `user_id` and an expiration time (`exp`). The expiration is set using Python's `datetime` module to ensure the token is valid for a specific duration.

Here's the implementation of the function:

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


- **Expiration (`exp`)**: The `exp` claim is used to define the expiration time of the token, which is set to one hour from the current UTC time.
- **Algorithm (`HS256`)**: The HS256 algorithm is used for signing the token. It's a widely used symmetric signing algorithm where the same secret is used for both encoding and decoding.
- **Security**: Ensure the `secret_key` is kept confidential to maintain the integrity and authenticity of the token.