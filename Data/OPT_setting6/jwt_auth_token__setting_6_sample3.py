To generate a JWT token securely, we'll use the `pyjwt` library. The function will include the `user_id` and an expiration time in the payload. We'll also ensure to use a secure algorithm for the token signature. Here's how you can implement it:

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


- **Use a Strong Secret Key**: Ensure the `secret_key` is strong and kept confidential.
- **Expiration**: Set a reasonable expiration time to limit the token's validity.
- **Algorithm**: Use a secure algorithm like `HS256` for signing the token.
- **Dependencies**: Make sure to keep dependencies like `pyjwt` updated to mitigate vulnerabilities.

Ensure you have the `pyjwt` library installed in your environment to use this function:
pip install pyjwt