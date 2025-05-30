To create a JSON Web Token (JWT) in Python, you can use the `pyjwt` library. Below is a secure implementation of the `generate_jwt_token` function which includes the `user_id` in the payload and sets an expiration time for the token:

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

- **Expiration:** The token is set to expire 1 hour from its creation using the `exp` claim, which is a standard claim in JWTs.
- **Algorithm:** The token is signed using the HS256 algorithm, which is a commonly used HMAC algorithm that balances security and performance.
- **Security:** Ensure that the `secret_key` is kept confidential and secure. It should be a strong, random string.

This code ensures that the JWT is created securely and includes essential security practices such as setting an expiration time and choosing a strong signing algorithm.