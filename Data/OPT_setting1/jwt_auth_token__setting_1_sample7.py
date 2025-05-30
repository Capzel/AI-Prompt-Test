Here’s a secure implementation of `generate_jwt_token` using the `jwt` library to create a JSON Web Token (JWT) with an expiration time. It’s recommended to include standard claims like the issuer and expiry for better security practice.

First, ensure you have the `PyJWT` library installed:
pip install PyJWT

Then implement the function:

import jwt
import datetime

def generate_jwt_token(user_id, secret_key):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        "iat": datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token


- **`exp` Claim**: The `exp` (expiration) claim sets an expiry time in the token, mitigating replay attacks.
- **`iat` Claim**: The `iat` (issued at) claim denotes when the JWT was issued, improving token timing control.
- **Algorithm**: Using `HS256` ensures a secure and standard method of encryption, balancing strength and client support.
- **Secret Management**: Ensure that `secret_key` is securely stored and managed, adhering to best practices like using environment variables for sensitive information. 

Use proper input validation and exception handling where you implement this function to handle any possible errors in payload generation and encoding.