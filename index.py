import sys
import os
 # add the path of detectron to your Projects
sys.path.append(os.getcwd())

import flask
from flask import render_template, request, make_response
from app import app
from routes.login import login
from routes.register import register


@app.route('/')
def index_route():
    # flask.abort(500)
    return render_template('index.html')


@app.route('/login', methods=['post', 'get'])
def login_route():
    return login(path=88)


@app.route('/register', methods=['get', 'post'])
def register_route():
    return register()




def main():
    app.run(port=8089, debug=True)


if __name__ == '__main__':
    main()
