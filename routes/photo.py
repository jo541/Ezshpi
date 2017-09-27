# -*-coding:UTF-8 -*
from flask import render_template, request
from . import app
from ..models.photo import Photo


@app.route('/photo',  methods=['POST'])
def photo():
    photos = Photo.query.all()
    if not request.form['code']:
        return render_template('index.html', message=u"Aucun code renseigné")
    return render_template('photo.html', photos=photos)

@app.route('/photo/new_photo')
def new_photo():
    return 'new Photo'

