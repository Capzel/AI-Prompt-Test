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


- **Expiration Time**: The `exp` claim is used to specify the expiration time of the token. This is crucial for security to ensure tokens are not valid indefinitely.
- **Algorithm**: The `HS256` algorithm is used for signing the token. Ensure that the secret key is kept secure and is sufficiently complex.
- **Library**: The `PyJWT` library is used to handle the encoding of the JWT. Make sure to install it using `pip install PyJWT` if you haven't already.

This implementation ensures that the token is securely generated and includes an expiration time to mitigate risks associated with token misuse.