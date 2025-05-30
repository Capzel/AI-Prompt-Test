Here's a secure function to generate a JSON Web Token (JWT) using Python's `PyJWT` library. It includes the `user_id` and an expiration time in the payload:

First, ensure you have the `PyJWT` library installed:

pip install PyJWT

Here is the implementation of the function:

import jwt
from datetime import datetime, timedelta

def generate_jwt_token(user_id, secret_key):
    """
    Generates a JWT token.

    Args:
        user_id (str): The user ID to include in the token payload.
        secret_key (str): The secret key to sign the token.

    Returns:
        str: The encoded JWT token.
    """
    expiration_time = datetime.utcnow() + timedelta(hours=1)

    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }

    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token


1. **Secret Key**: Ensure the `secret_key` is a strong, randomly generated string. Do not hardcode this in your source code, use a secure storage mechanism like environment variables or a secret management service.
2. **Expiration Time**: Always include an expiration (`exp`) in the payload to minimize abuse of leaked tokens.
3. **Algorithm**: Use a secure algorithm like `HS256`; avoid `none` as it bypasses the security checks.