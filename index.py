import sys
import os
 # add the path of detectron to your Projects
sys.path.append(os.getcwd())

import flask
from flask import render_template, request, make_response
from app import app
from routes import login,register,home,\
    class_manage,stu_manage
@app.route('/')
def index_route():
    # flask.abort(500)
    return render_template('index.html')


@app.route('/login', methods=['post', 'get'])
def login_route():
    return login.login(path=88)

@app.route('/register', methods=['get', 'post'])
def register_route():
    return register.register()

@app.route('/home', methods=['get', 'post'])
def home_route():
    return home.home()

@app.route('/class_manage', methods=['get', 'post'])
def class_manage_route():
    return class_manage.class_manage()

@app.route('/stu_manage', methods=['get', 'post'])
def stu_manage_route():
    return stu_manage.stu_manage()




def main():
    app.run(port=8089, debug=True)


if __name__ == '__main__':
    main()
