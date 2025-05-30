To create a JWT token securely, you can use the `PyJWT` library, which is a popular choice for handling JWTs in Python. Below is a function `generate_jwt_token` that generates a JWT token with a payload containing the `user_id` and an expiration time. The expiration time is set to a reasonable default, such as 1 hour from the time of token generation.

First, ensure you have the `PyJWT` library installed:

pip install PyJWT

Here's the function:

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


- **Expiration Time**: The token includes an expiration (`exp`) claim to ensure it is valid only for a limited time, reducing the risk of misuse.
- **Algorithm**: The token is signed using the HS256 algorithm, which is a secure and commonly used choice for JWTs.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.

This function provides a secure way to generate JWT tokens, adhering to best practices for token expiration and signing.