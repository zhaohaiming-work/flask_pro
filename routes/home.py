import flask
from flask import render_template, request, make_response,flash,redirect


def home(**key):
    # print(request.method)
    menu = [
      {
        'title':'班级管理',
        'url':'class_manage'
      },
      {
        'title':'学生管理',
        'url':'stu_manage'
      }
    ]
    return render_template('home.html',menu=menu)
