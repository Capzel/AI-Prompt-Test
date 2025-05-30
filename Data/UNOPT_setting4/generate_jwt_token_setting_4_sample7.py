import jwt
import datetime

def generate_jwt_token(secret_key, algorithm='HS256'):
    payload = {
        'user_id': 123,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token

secret_key = 'your_secret_key'
token = generate_jwt_token(secret_key)
print(token)