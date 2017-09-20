
# -*-coding:UTF-8 -*
from flask import render_template, request
from . import app

@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')
