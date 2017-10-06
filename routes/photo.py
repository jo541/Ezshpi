# -*-coding:UTF-8 -*
from flask import render_template, request
from werkzeug.security import check_password_hash
from . import app
from ..models.photo import Photo
from ..models.users import Users


@app.route('/photo',  methods=['POST'])
def photo():
    photos = Photo.query.all()
    password = request.form['password']
    username = request.form['username']
    admin = False
    if not password or not username:
        return render_template('index.html', message=u"Aucun nom utilisateur ou mot de passe renseigné")
    user = Users.query.filter_by(username=request.form['username']).first()
    if user.id == 1:
        admin = True
    if user and check_password_hash(user.password, password):
    	return render_template('photo.html', photos=photos, admin=admin)
    else:
    	return render_template('index.html', message=u"Erreur utilisateur ou mdp inconnu")

@app.route('/photo/photo_manager')
def photo_manager():
    return render_template('photo_manager.html')

@app.route('/photo/photo_manager/add_photo')
def add_photo():
    return render_template('photo_manager.html', information="Add Photo")

@app.route('/photo/photo_manager/remove_photo')
def remove_photo():
    return render_template('photo_manager.html', information="Remove Photo")
