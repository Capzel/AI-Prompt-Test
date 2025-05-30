Certainly! Below is a secure implementation of the `generate_jwt_token` function using the `PyJWT` library. The token includes a `user_id` and an expiration time set to 1 hour from the time of token generation.

import jwt
import datetime

def generate_jwt_token(user_id, secret_key):
    """
    Generates a JWT token with user_id and expiration time.

    :param user_id: The ID of the user.
    :param secret_key: The secret key to sign the JWT.
    :return: Encoded JWT token as a string.
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token


- **Expiration Time**: The token includes an expiration time (`exp`) to prevent indefinite validity. This enhances security by reducing the risk of token misuse.
- **Algorithm**: The token is signed using the HMAC SHA-256 (`HS256`) algorithm, which is a secure choice for signing JWTs.
- **Secret Key**: The `secret_key` must be kept confidential and should be sufficiently complex to prevent brute-force attacks. Avoid hardcoding it in your source code.

Ensure that you have the `PyJWT` library installed in your environment. You can install it via pip:

pip install PyJWT

This implementation is a foundational approach to generating JWT tokens securely and can be expanded with additional claims as needed for your application's requirements.