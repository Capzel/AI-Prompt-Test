import jwt
import datetime

def generate_jwt_token(user_id, secret_key):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

user_id = '12345'
secret_key = 'your_secret_key'
token = generate_jwt_token(user_id, secret_key)
print(token)