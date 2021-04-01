import flask
from flask import render_template, request, make_response,flash,redirect

from ORM.user import User,db

from app.token_auth import create_auth_token

def login(**key):
    # print(request.method)
    if request.method == 'POST':
        data = request.form
        user_name = str.strip(data.get('user_name') or '')
        password = data.get('password')
        if user_name =='' or password=='':
            flash('请填完整信息')
        else:
            user = User.query.filter(User.user_name==user_name).first()
            print(user)
            if user:
                if user.check_password(password):
                  # 设置cookie
                  token =create_auth_token(user.id).decode('utf-8')
                  # print(user.id,token)
                  respose = make_response(redirect('/'))
                  respose.set_cookie('_t', token)
                  return  respose
                else:
                    flash('密码输入有误')
            else:
                flash('此用户不存在')


    return render_template('login.html')
