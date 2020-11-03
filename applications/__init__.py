from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DATABASE_URL')
app.config["SECRET_KEY"] = environ.get('SECRET_KEY')

db.init_app(app)
login_manager.init_app(app)




from applications import routes 