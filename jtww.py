import jwt
import datetime

def create_token(payload, secret_key, expiration_minutes):
    current_time_utc = datetime.datetime.utcnow()
    payload['iat'] = current_time_utc
    expiration_time = current_time_utc + datetime.timedelta(minutes=expiration_minutes)
    payload['exp'] = expiration_time
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def decode_token(token, secret_key):
    try:
        decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        print("Токен втратив чинність.")
        return None
    except jwt.InvalidTokenError:
        print("Недійсний токен.")
        return None

secret_key = "secret_key_here"

user_data = {
    'user_id': 12345,
    'username': 'john_doe',
    'email': 'john.doe@example.com',
}

token_lifetime_minutes = 15

token = create_token(user_data, secret_key, token_lifetime_minutes)
print("Створений токен:", token)

decoded_data = decode_token(token, secret_key)
if decoded_data:
    print("Розкодовані дані користувача:", decoded_data)
