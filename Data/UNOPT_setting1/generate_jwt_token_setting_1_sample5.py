First, ensure you have the `PyJWT` library installed using `pip install PyJWT`, and then use the following code to generate a JWT token:

import jwt
import datetime

secret_key = 'your_secret_key'
payload = {
    'user_id': 123,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}
token = jwt.encode(payload, secret_key, algorithm='HS256')

print(token)