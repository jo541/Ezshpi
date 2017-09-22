# -*-coding:UTF-8 -*
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists, create_database
import routes
import models

# Init application and db object
app = Flask(__name__)
app.register_blueprint(routes.app)

# DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tojo:tiger@localhost:5432/easy_share'
db = SQLAlchemy(app)
# Check if db exists if not create it 
if not database_exists('postgresql://tojo:tiger@localhost:5432/easy_share'):
	create_database('postgresql://tojo:tiger@localhost:5432/easy_share')
db.create_all()

# Create admin user
from models.users import Users
if not Users.query.filter_by(username='admin').first():
	admin = Users('admin', 'admin@example.com')
	db.session.add(admin)
	db.session.commit()

if __name__ == "__main__":
    app.run()
