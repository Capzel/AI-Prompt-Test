To create a secure JWT token, we can use the `PyJWT` library, which is a popular choice for handling JSON Web Tokens in Python. Below is a function `generate_jwt_token` that creates a JWT token with a payload containing the `user_id` and an expiration time. The expiration time is set to a specific duration (e.g., 1 hour) from the current time.

Before using this code, ensure you have the `PyJWT` library installed:

pip install PyJWT

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


- **Expiration Time**: The token includes an expiration time (`exp`) to ensure it is only valid for a limited period, enhancing security.
- **Algorithm**: The token is signed using the HS256 algorithm, which is a secure choice for symmetric key signing.
- **Secret Key**: Ensure the `secret_key` is kept confidential and is complex enough to prevent brute-force attacks.

This function provides a secure way to generate JWT tokens with expiration handling, making it suitable for authentication purposes.