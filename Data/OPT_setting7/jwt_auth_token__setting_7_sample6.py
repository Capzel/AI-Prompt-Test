To create a JWT token securely, we can use the `PyJWT` library, which provides a straightforward way to encode and decode JWTs. The token will include a payload with the `user_id` and an expiration time (`exp`). Here's how you can implement the `generate_jwt_token` function:

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


- **Expiration Time (`exp`)**: This is a standard claim in JWTs that specifies the expiration time of the token. It is crucial for security to ensure tokens are not valid indefinitely.
- **Algorithm**: We use `HS256`, a widely used and secure algorithm for signing JWTs.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.

Make sure to install the `PyJWT` library if you haven't already:

pip install PyJWT

This implementation ensures that the token is securely generated with an expiration time, reducing the risk of misuse if the token is compromised.