To create a secure JWT token in Python, you can use the `PyJWT` library. The function `generate_jwt_token` will include the `user_id` and an expiration time in the payload. Here's how you can implement it:

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


- **Expiration Time**: The token includes an expiration time (`exp`) to ensure it is only valid for a limited period, reducing the risk of misuse.
- **HS256 Algorithm**: The token is signed using the HS256 algorithm, which is a secure HMAC-based signing method.
- **Security**: Always use a strong, unpredictable secret key to prevent unauthorized token creation or tampering.
- **Dependencies**: Ensure you have the `PyJWT` library installed (`pip install PyJWT`).