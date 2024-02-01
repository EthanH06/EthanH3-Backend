from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)

# Configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Use environment variable or a default value for database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///volumes/sqlite.db')

# Secret Key
SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY

# SQLAlchemy and Migration
db = SQLAlchemy(app)
Migrate(app, db)

# Images storage
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # maximum size of uploaded content
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']  # supported file types
app.config['UPLOAD_FOLDER'] = 'volumes/uploads/'  # location of user uploaded content
