To create a secure JWT token, we can use the `PyJWT` library, which is a popular choice for handling JSON Web Tokens in Python. The token will include a payload with the `user_id` and an expiration time (`exp`). Here's how you can implement the `generate_jwt_token` function:

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


- **Expiration Time**: The `exp` claim is used to specify the expiration time of the token. It's set to one hour from the current time using `datetime.timedelta`.
- **Algorithm**: The token is signed using the HS256 algorithm, which is a symmetric algorithm requiring a secret key.
- **Security**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.
- **Library**: You need to install the `PyJWT` library if you haven't already, using `pip install PyJWT`.

This function generates a JWT token that is secure and includes an expiration time to prevent indefinite validity.