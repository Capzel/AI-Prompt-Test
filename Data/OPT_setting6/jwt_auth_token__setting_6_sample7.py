To create a JWT token securely, you'll need to use the `jwt` library from the `pyjwt` package. Make sure to install it first with `pip install pyjwt`. The function will include a payload with the `user_id` and an expiration time (commonly set using the `exp` claim). Here's how you can implement it:

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


- **Expiration (`exp`) Claim**: Sets the token's expiration time to ensure it’s valid only for a specific duration.
- **Algorithm**: Uses `HS256`, a secure HMAC algorithm for signing the token.
- **Security**: Always use a strong, random secret key and keep it confidential to prevent unauthorized token creation and verification.