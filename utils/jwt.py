# 自定义jwt认证成功返回数据
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }