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


- **Expiration Time**: The `exp` claim is used to specify the expiration time of the token. It's important to set this to ensure tokens are not valid indefinitely.
- **Algorithm**: The `HS256` algorithm is used for signing the token. Ensure that the secret key is kept secure and is sufficiently complex.
- **Security**: Always validate and verify the token on the server side when it is received to ensure it hasn't been tampered with.