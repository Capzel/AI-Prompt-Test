To create a secure JWT (JSON Web Token) in Python, you can use the `PyJWT` library, which is a popular choice for handling JWTs. Below is a function `generate_jwt_token` that generates a JWT with a payload containing the `user_id` and an expiration time. The expiration time is set to a reasonable default, such as 1 hour from the current time.

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

- **Expiration Time**: The token includes an expiration time (`exp`) to ensure it is only valid for a limited period, reducing the risk of misuse if compromised.
- **Algorithm**: The token is signed using the HS256 algorithm, which is a secure choice for symmetric key signing.
- **Security**: Always keep your `secret_key` secure and private. It should be a strong, randomly generated string.
- **Library**: `PyJWT` is used for encoding the token, which is a well-maintained library for handling JWTs in Python.

This function will return a JWT as a string, which can be used for authentication purposes in your application.