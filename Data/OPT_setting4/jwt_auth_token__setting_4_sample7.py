To create a secure JSON Web Token (JWT) in Python, you can use the `PyJWT` library. This library allows you to encode and decode JWTs easily. Below is a function `generate_jwt_token` that generates a JWT with a payload containing the `user_id` and an expiration time. The expiration time is set to a specific duration from the current time, ensuring the token is valid only for a limited period.

Here's the code for the function:

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


- **Expiration Time**: The token includes an expiration time (`exp`) set to one hour from the current time. This ensures the token is only valid for a limited period, reducing the risk of misuse.
- **HS256 Algorithm**: The token is signed using the HS256 algorithm, which is a secure choice for symmetric key signing.
- **Secret Key**: Ensure that the `secret_key` is kept secure and is not hard-coded in your source code. Consider using environment variables or a secure vault for managing secrets.

This function provides a secure way to generate JWT tokens, adhering to best practices for token expiration and signing.