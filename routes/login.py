import flask
from flask import render_template, request, make_response


def login(**key):
    print(request.method)
    if request.method == 'POST':
        print(dict(request.form))
    return render_template('login.html')
