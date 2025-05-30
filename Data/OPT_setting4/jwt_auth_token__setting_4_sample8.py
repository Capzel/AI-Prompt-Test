To generate a JWT token securely, we can use the `PyJWT` library, which is a popular choice for handling JSON Web Tokens in Python. The token will include a payload with the `user_id` and an expiration time (`exp`). Here's how you can implement the `generate_jwt_token` function:

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


- **Expiration Time**: The `exp` claim is used to set the expiration time of the token. This ensures that the token is only valid for a limited period, reducing the risk of misuse if it gets compromised.
- **Algorithm**: We use `HS256`, a secure HMAC-based algorithm, for signing the token. Ensure that the `secret_key` is kept confidential and is sufficiently complex.
- **Security**: Always validate the token on the server side before trusting any information it contains. This includes checking the signature and the expiration time.