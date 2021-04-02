import flask
from flask import render_template, request, make_response,flash,redirect

from .common_data import menu
def class_manage(**key):
    # print(request.method)
    
    return render_template('class_manage.html',menu=menu)
