# -*-coding:UTF-8 -*
from flask import Flask
import routes

app = Flask(__name__)
app.register_blueprint(routes.app)

if __name__ == "__main__":
    app.run()
