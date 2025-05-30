To create a JWT token securely, we'll use the `pyjwt` library, which is a popular choice for handling JWTs in Python. The function will include the `user_id` in the payload and set an expiration time to ensure the token is valid only for a limited period. Here's how you can implement the `generate_jwt_token` function:

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


- **Expiration Time**: The token includes an expiration time (`exp`) to ensure it is valid only for a specified duration, reducing the risk of misuse.
- **Algorithm**: We use the `HS256` algorithm, which is a secure choice for signing JWTs.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.
- **Library**: `pyjwt` is a well-maintained library that simplifies JWT handling and should be installed via `pip install pyjwt` if not already available.