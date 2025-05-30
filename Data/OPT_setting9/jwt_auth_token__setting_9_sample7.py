To create a secure JWT token, you can use the `PyJWT` library, which is a popular choice for handling JWTs in Python. The token will include a payload with the `user_id` and an expiration time (`exp`). Here's how you can implement the `generate_jwt_token` function:

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


- **Expiration Time**: The `exp` claim is used to specify the expiration time of the token. It is set to one hour from the current UTC time.
- **Algorithm**: The token is signed using the HS256 algorithm, which is a secure choice for symmetric key signing.
- **Security**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.