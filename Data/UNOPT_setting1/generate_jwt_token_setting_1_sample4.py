import jwt
import datetime

secret_key = 'your_secret_key'
user_id = 'user123'

token = jwt.encode(
    {'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
    secret_key,
    algorithm='HS256'
)

print(token)