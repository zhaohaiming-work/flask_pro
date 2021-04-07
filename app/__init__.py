import flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import request,make_response
from .token_auth import verify_auth_token
from flask import flash,redirect
from .token_require import token_require_path
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
app = flask.Flask(__name__, template_folder='../templates',
                  static_folder='../static')
CORS(app, supports_credentials=True)


bcrypt.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zhm1072950174@127.0.0.1:3306/teaching'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'FDSAFDSFDSFADSF'

CSRFProtect(app)

db = SQLAlchemy(app)

# 每次请求都会执行
@app.before_request
def before_request():
    token = request.cookies.get('_t')
    # print(request.path)
    path = request.path
    method = request.method
    for route in token_require_path:
        p = route.get('path')
        m = route.get('method')
        if p == path and m == method:
            if token:
                t=verify_auth_token(token)
                if  not t:
                    return redirect('login')
            else:
                return redirect('login')



@app.errorhandler(500)
def server_error(e):
    print(e)
    return '%s' % e,500

@app.errorhandler(404)
def page_notfount(e):
    print(e)
    return '页面未找到 %s'%request.path,400

@app.errorhandler(Exception)
def exception_error(e):
    return e,500