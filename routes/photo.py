# -*-coding:UTF-8 -*
from flask import render_template, request
from . import app

@app.route('/photo',  methods=['POST'])
def photo():
    if not request.form['code']:
        return render_template('index.html', message=u"Aucun code renseigné")
    return render_template('photo.html')
