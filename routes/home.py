import flask
from flask import render_template, request, make_response,flash,redirect

from .common_data import menu
def home(**key):
    # print(request.method)
    
    return render_template('home.html',menu=menu)
