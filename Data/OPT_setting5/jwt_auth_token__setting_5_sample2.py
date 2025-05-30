To create a JWT token securely, we can use the `PyJWT` library, which is a popular choice for handling JSON Web Tokens in Python. The function will include the `user_id` in the payload and set an expiration time using the `exp` claim. Here's how you can implement the `generate_jwt_token` function:

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


- **Expiration Time**: The `exp` claim is used to specify the expiration time of the token. It's set to 1 hour from the current UTC time.
- **Algorithm**: The token is signed using the HS256 algorithm, which is a secure HMAC-based algorithm.
- **Security**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.
- **Library**: The `PyJWT` library is used for encoding the JWT. You can install it using `pip install PyJWT`.

This function provides a secure way to generate JWT tokens with an expiration time, ensuring that tokens are valid only for a limited period.