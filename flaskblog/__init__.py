from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_basicauth import BasicAuth



app = Flask(__name__)
app.config['SECRET_KEY'] = '5731628ba0f13ce0c643fde283baw451'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'

db = SQLAlchemy(app)

admin = Admin(app, name='Admin Panel')

basic_auth = BasicAuth(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'dark'

from flaskblog import routes
