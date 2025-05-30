import jwt
import datetime

def generate_jwt_token(secret_key):
    payload = {
        'user': 'example_user',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

secret_key = 'your_secret_key'
token = generate_jwt_token(secret_key)
print(token)