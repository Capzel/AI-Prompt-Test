Sure, here's a simple example of generating a JWT token in Python using the `PyJWT` library:

import jwt
import datetime

def generate_jwt(user_id, secret_key):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token

user_id = '123456'
secret_key = 'your_secret_key'
token = generate_jwt(user_id, secret_key)

print(token)

Make sure you have the PyJWT library installed by running `pip install pyjwt`.