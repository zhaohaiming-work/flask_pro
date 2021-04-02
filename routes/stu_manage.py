import flask
from flask import render_template, request, make_response,flash,redirect

from .common_data import menu
def stu_manage(**key):
    # print(request.method)
    
    return render_template('stu_manage.html',menu=menu)
