To create a secure JWT token, we can use the `PyJWT` library, which is a popular choice for handling JSON Web Tokens in Python. The token will include a payload with the `user_id` and an expiration time (`exp`). The expiration time should be set to a reasonable duration to ensure the token's validity is limited.

Here's how you can implement the `generate_jwt_token` function:

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


- **Expiration Time (`exp`)**: The token includes an expiration time to limit its validity. This is a crucial security measure to prevent long-term misuse if the token is compromised.
- **Algorithm**: We use the `HS256` algorithm, which is a secure and commonly used HMAC-based signing algorithm.
- **Secret Key**: Ensure that the `secret_key` is kept confidential and is sufficiently complex to prevent brute-force attacks.

Before using this function, make sure to install the `PyJWT` library if you haven't already:

pip install PyJWT

This implementation ensures that the JWT token is securely generated and encoded, adhering to best practices for token-based authentication.