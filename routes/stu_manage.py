import flask
from flask import render_template, request, make_response,flash,redirect

from .common_data import menu

from ORM.stu_manage import db,Stu_manage
from sqlalchemy import or_
def stu_manage(**key):
    try:
      args = request.args
      name = args.get('name')
      code = args.get('code')
      filters = []
      # 需要用拼接的方法
      if name:
        filters.append(Stu_manage.stu_name==name)
      if code:
        filters.append(Stu_manage.class_code==code)
      stus = Stu_manage.query.filter(*filters).all()
      print(stus)
    except Exception as e:
      print(e)
    finally:
      return render_template('stu_manage.html',menu=menu,\
        stu_list=stus,stu_name=name,class_code=code)

def stu_manage_search(**key):
    # print(request.form)
    req = request.form
    stu_name = req.get('stu_name')
    class_code = req.get('class_code')
    # stus = Stu_manage.query.filter().all()
    print(stu_name,class_code)
    return redirect('/stu_manage?name=%s&code=%s'%(stu_name,class_code))

def stu_manage_del(**key):
    try:
      req = request.args
      id_ = req.get('id')
      stus = Stu_manage.query.get(int(id_))
      if stus:
        db.session.delete(stus)
        db.session.commit()
        print('删除成功')
    except Exception as e:
      print(e)
    return redirect('/stu_manage')
