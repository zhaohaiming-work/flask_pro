import flask
from flask import render_template, request, make_response,flash,redirect

from .common_data import menu

from ORM.stu_manage import db,Stu_manage
from sqlalchemy import or_
from app import app

@app.route('/stu_manage', methods=['get', 'post'])
def stu_manage(**key):
    try:
      args = request.args
      name = args.get('name') or ''
      code = args.get('code') or ''
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

@app.route('/stu_manage/search', methods=['post'])
def stu_manage_search(**key):
    # print(request.form)
    req = request.form
    stu_name = req.get('stu_name')
    class_code = req.get('class_code')
    # stus = Stu_manage.query.filter().all()
    print(stu_name,class_code)
    return redirect('/stu_manage?name=%s&code=%s'%(stu_name,class_code))

@app.route('/stu_manage/del')
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

@app.route('/stu_manage_handle/<type>',methods=['post','get'])
def stu_manage_handle(type):
    print(request.args.get('id'))
    # flash('欢迎使用')
    try:
      if request.method=='GET':
       return render_template('stu_manage_handle.html',menu=menu,type=type)
      # 判断是不是新增
      if type=='add':
        req = request.form
        stu_name = req.get('stu_name')
        class_code = int(req.get('class_code'))
        if stu_name=='':
          flash('姓名不为空')
          return render_template('stu_manage_handle.html',menu=menu,type=type)
        # 查询看是否有重名的
        stu = Stu_manage.query.filter(Stu_manage.stu_name==stu_name,\
          Stu_manage.class_code==class_code).first()

        if stu:
          flash('学生已经存在')
          return render_template('stu_manage_handle.html',menu=menu,type=type)
        else:
          # 如果没有重名则添加数据库
          stu_modle = Stu_manage(
            stu_name=req.get('stu_name'),\
            class_code=req.get('class_code'),\
            gender=req.get('gender'),\
            age= int(req.get('age')) if req.get('age') else None,\
            height= int(req.get('height')) if req.get('height') else None,\
            weight= int(req.get('weight')) if req.get('weight') else None
            )
          db.session.add(stu_modle)
          db.session.commit()
          return redirect('/stu_manage')
      else:
        req = request.form

        print(request.args.get('id'))
        return render_template('stu_manage_handle.html',menu=menu,type=type)
    except Exception as e:
      print(e)
      return render_template('stu_manage_handle.html',menu=menu,type=type)

