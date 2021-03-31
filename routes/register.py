import flask

from flask import render_template, request, flash

from ORM.user import User
from app import db
def register(*key, **kw):

    if request.method == 'POST':
        data = dict(request.form)
        # print(User)
        user_name = str.strip(data.get('user_name') or '')
        password = data.get('password')
        if user_name == '' or password == '':
            flash('请填写用户信息')
        else:
            name =User.query.filter(User.user_name==user_name).first()
            if name :
                flash('该用户已经存在，请直接登录')
            else:
                user = User(user_name=user_name,password=password)
                db.session.add(user)
                db.session.commit()
                flash('注册成功，请登录')

    return render_template('register.html')
