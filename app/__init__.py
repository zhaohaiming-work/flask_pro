import flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask import request,make_response
app = flask.Flask(__name__, template_folder='../templates',
                  static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zhm1072950174@127.0.0.1:3306/teaching'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'FDSAFDSFDSFADSF'

CSRFProtect(app)

db = SQLAlchemy(app)


@app.errorhandler(500)
def page_error(e):
    print(e)
    return '%s' % e,500

@app.errorhandler(404)
def page_notfount(e):
    print(e)
    return '页面未找到 %s'%request.path,400
