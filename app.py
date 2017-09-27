# -*-coding:UTF-8 -*
#Standar import 
from flask import Flask
import base64
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists, create_database




# Init application 
app = Flask(__name__)
# DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tojo:tiger@localhost:5432/easy_share'
db = SQLAlchemy(app)

# Check if db exists if not create it 
if not database_exists('postgresql://tojo:tiger@localhost:5432/easy_share'):
	create_database('postgresql://tojo:tiger@localhost:5432/easy_share')

# import all models and create it
import models
db.create_all()

#Import all routes and generate it
import routes
app.register_blueprint(routes.app)


def create(record):
	db.session.add(record)
	db.session.commit()
	
# Create admin user
from models.users import Users
from models.photo import Photo
if not Users.query.filter_by(username='admin').first():
	create(Users('admin', 'admin@example.com'))
if not Photo.query.filter_by(name='photo1').first():
	with open("/Users/tojo/Personel/easy_photo_share/static/images/portfolio/1.jpg", "rb") as image_file:
		create(Photo('photo1', base64.b64encode(image_file.read())))
	with open("/Users/tojo/Personel/easy_photo_share/static/images/portfolio/2.jpg", "rb") as image_file:
		create(Photo('photo2', base64.b64encode(image_file.read())))
	with open("/Users/tojo/Personel/easy_photo_share/static/images/portfolio/3.jpg", "rb") as image_file:
		create(Photo('photo3', base64.b64encode(image_file.read())))


if __name__ == "__main__":
    app.run()
