import jwt
import datetime

SECRET_KEY = 'your_secret_key'
user_id = 123

payload = {
    'user_id': user_id,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
    'iat': datetime.datetime.utcnow()
}

token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
print(token)