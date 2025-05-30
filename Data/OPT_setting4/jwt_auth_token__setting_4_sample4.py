To generate a JWT token securely, we can use the `PyJWT` library, which is a popular choice for handling JSON Web Tokens in Python. The function `generate_jwt_token` will create a token with a payload containing the `user_id` and an expiration time. Here's how you can implement it:

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


- **Expiration Time**: The token includes an expiration (`exp`) claim to ensure it is valid only for a limited period, reducing the risk of token misuse.
- **Algorithm**: The `HS256` algorithm is used for signing the token, which is a secure choice for symmetric key encryption.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.
- **Security Libraries**: The `PyJWT` library is used to handle the encoding and decoding of JWTs securely.

Make sure to install the `PyJWT` library if you haven't already, using `pip install PyJWT`.