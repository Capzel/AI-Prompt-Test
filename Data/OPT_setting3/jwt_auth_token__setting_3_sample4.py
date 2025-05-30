To create a JWT token securely, we can use the `PyJWT` library, which is a popular choice for handling JSON Web Tokens in Python. The function `generate_jwt_token` will include the `user_id` and an expiration time in the payload. We'll use the `HS256` algorithm for signing the token, which is a secure choice for symmetric key encryption.

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


- **Expiration Time**: The token includes an expiration time (`exp`) to ensure it is only valid for a limited period, reducing the risk of misuse if compromised.
- **Algorithm**: We use `HS256`, a secure hashing algorithm, to sign the token.
- **Secret Key**: Ensure the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.
- **Security**: Always validate the token on the server side before trusting any information it contains.