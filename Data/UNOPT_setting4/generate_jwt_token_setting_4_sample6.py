import jwt
import datetime

def generate_jwt(user_id, secret, algorithm='HS256'):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token

secret_key = 'your_secret_key'
user_id = '12345'
token = generate_jwt(user_id, secret_key)
print(token)