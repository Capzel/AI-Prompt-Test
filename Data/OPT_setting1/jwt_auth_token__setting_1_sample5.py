To create a JSON Web Token (JWT) in a secure way, we can use the `pyjwt` library. The function `generate_jwt_token` will include a payload with the `user_id` and set an expiration time. Below is the implementation:

import jwt
from datetime import datetime, timedelta

def generate_jwt_token(user_id, secret_key):
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    
    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }

    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token


1. **Expiration Time**: The token includes an `exp` claim which dictates when the token should expire. This helps mitigate risks related to stolen tokens being used indefinitely.
   
2. **Secure Encoding**: The `HS256` (HMAC with SHA-256) algorithm is specified for encoding the token to ensure it is cryptographically secured.

3. **Dependencies**: Ensure that the `pyjwt` library is installed, as it's used to create the token (`pip install pyjwt`).

By following best practices in security and keeping the functions simple and scalable, you're ready to implement token-based authentication efficiently.