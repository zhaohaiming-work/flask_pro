import flask

from flask import render_template, request, flash

from ORM.user import User,db

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
                try:
                    user = User(user_name=user_name)
                    user.set_password(password)
                    db.session.add(user)
                    db.session.commit()
                    flash('注册成功，请登录')
                except Exception as e:
                    print(e)

    return render_template('register.html')
