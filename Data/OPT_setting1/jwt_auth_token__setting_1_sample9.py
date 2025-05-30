To create a securely encoded JWT token, you can utilize the `PyJWT` library, which helps ensure that tokens are signed and verified securely. Ensure you have installed the library via pip:

pip install PyJWT

Here's how you can implement the `generate_jwt_token` function that uses PyJWT to create a JWT token with a payload including `user_id` and `expiration` time. The `exp` claim is used to indicate the expiration time and is set safely by using the UTC timezone to avoid issues with daylight saving time or time zone interactions.

import jwt
import datetime
from typing import Union

def generate_jwt_token(user_id: Union[int, str], secret_key: str) -> str:
    """
    Generates a JWT token for the given user ID, signed with the provided secret key.

    :param user_id: The ID of the user for whom to create the token. Can be string or integer.
    :param secret_key: The secret key to sign the token.
    :return: The encoded JWT token as a string.
    """
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    
    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token if isinstance(token, str) else token.decode('utf-8')



1. **Payload**:  
   - Includes `user_id` and `exp`, where `exp` (expiration) is set to one hour ahead of the current UTC time.

2. **Secret Key**:  
   - Use a robust, unpredictable secret key to sign the JWT. In practice, changes to this key should be carefully migrated.

3. **HS256 Algorithm**:  
   - A commonly used, secure signing algorithm; ensure your audience verifies it properly during token issuance checks.

4. **UTC for Expiry**:
   - Use `datetime.datetime.utcnow()` to handle time in a global standard avoiding localized time issues.

5. **Encoding Output Type**:
   - JWT output from `jwt.encode(...)` can be bytes in some contexts, so it's prudent to return a uniform string, hence the conditional decoding.