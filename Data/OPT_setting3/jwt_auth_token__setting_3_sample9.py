To create a JWT token securely, we can use the `pyjwt` library, which is a popular choice for handling JSON Web Tokens in Python. The function will include the `user_id` and an expiration time in the payload. Here's how you can implement the `generate_jwt_token` function:

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
- **Algorithm**: The token is signed using the HS256 algorithm, which is a secure choice for symmetric key signing.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.
- **Library**: The `pyjwt` library is used for encoding the JWT, which handles the token creation and signing process securely.

Make sure to install the `pyjwt` library if you haven't already:

pip install pyjwt

This implementation provides a secure way to generate JWT tokens with user-specific data and expiration handling.