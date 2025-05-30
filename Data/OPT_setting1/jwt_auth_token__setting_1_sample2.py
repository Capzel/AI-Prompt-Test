Certainly! To create a JSON Web Token (JWT) in Python, we can use the `PyJWT` library. Here's a sample implementation of the `generate_jwt_token` function. This function includes the `user_id` and sets an expiration time for the token:

import jwt
import datetime

def generate_jwt_token(user_id, secret_key):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token is valid for 1 hour

    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }

    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token


1. **Security**: Ensure that `secret_key` is generated securely and kept confidential. It should be long enough and ideally use a random sequence of characters.
2. **Claims**: We included `exp` to specify an expiration time, enhancing the security of the token by making it valid only for a set duration.
3. **Algorithm**: Always specify the hashing algorithm (`HS256` in this case) for signing the token.
4. **Dependency**: You need to install the `PyJWT` library (`pip install PyJWT`) before using this function.