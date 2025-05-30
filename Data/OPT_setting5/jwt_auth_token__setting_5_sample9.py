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


- **Expiration Time**: The `exp` claim is used to set the expiration time of the token, which helps in ensuring that the token is valid only for a specific duration.
- **Algorithm**: The `HS256` algorithm is used for signing the token, which is a secure choice for symmetric key signing.
- **Security**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.
- **Library**: The `PyJWT` library is used for encoding the JWT, which you can install via `pip install PyJWT`.

This implementation ensures that the token is secure and includes an expiration time to mitigate risks associated with token reuse.