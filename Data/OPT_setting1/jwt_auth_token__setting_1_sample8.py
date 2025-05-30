Sure! Let's create a function to generate a JWT token. To do this securely, we'll use the PyJWT library, which is a commonly used library for handling JWT tokens in Python.

First, make sure you have the PyJWT library installed:

pip install PyJWT

Now, let's implement the function:

import jwt
import datetime

def generate_jwt_token(user_id, secret_key):
    try:
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
        }

        token = jwt.encode(payload, secret_key, algorithm='HS256')

        if isinstance(token, bytes):
            token = token.decode('utf-8')

        return token
    except Exception as e:
        print(f"An error occurred while generating the token: {e}")
        return None

- **Import Libraries**: We import `jwt` from the PyJWT package and `datetime` for handling the expiration time.
- **Payload**: This includes the `user_id` as part of the token and sets an expiration (`'exp'`) for 1 hour from the creation time.
- **Token Encoding**: The `jwt.encode` method is used to create the token with the given payload, secret key, and HMAC algorithm (`HS256`), which is a popular asymmetric cryptographic signing method.
- **Error Handling**: We used a try-except block to handle any issues that may arise during token generation, ensuring that any exception details are logged correctly.

This function returns a securely generated JWT token with a specific expiration period, helping protect against JWT-related vulnerabilities when used correctly.