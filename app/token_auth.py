from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth(scheme='JWT')

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# 密钥，可随意修改
SECRET_KEY = 'techingproject'
# 生成token, 有效时间为600min
def create_auth_token(user_id, expiration=36000):
    # 第一个参数是内部私钥
    # 第二个参数是有效期（秒）
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return s.dumps({'user_id': user_id})


# 解析token
@auth.verify_password
def verify_auth_token(token):
    s = Serializer(SECRET_KEY)
    # token正确
    try:
        data = s.loads(token)
        return data
    # token过期
    except SignatureExpired:
        return None
    # token错误
    except BadSignature:
        return None

@auth.error_handler
def error_handler():
    return '无服务'