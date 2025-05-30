import jwt
import datetime

def create_jwt_token(user_id, secret_key):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token