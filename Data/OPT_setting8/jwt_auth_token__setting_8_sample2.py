To create a secure JWT token in Python, we can use the `PyJWT` library. This library allows us to encode and decode JSON Web Tokens (JWT). Below is a function `generate_jwt_token` that generates a JWT token with a payload containing the `user_id` and an expiration time. We'll set the expiration time to 1 hour from the time of token generation.

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
- **Algorithm**: We use the `HS256` algorithm, which is a secure and commonly used algorithm for signing JWTs.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.

This function provides a secure way to generate JWT tokens with a user identifier and expiration, following best practices for token-based authentication.