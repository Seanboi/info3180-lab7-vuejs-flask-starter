from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lab5_user:lab5@localhost:8080/lab5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'


# Creates an 'uploads' folder in the same directory as your app
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

# Ensures the uploads folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
    


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views