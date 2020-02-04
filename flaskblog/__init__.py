from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_mail import Mail
from flaskblog.config import Config


mail = Mail()

db = SQLAlchemy()

admin = Admin(name='Admin Panel')

basic_auth = BasicAuth()

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'dark'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)
    db.init_app(app)
    admin.init_app(app)
    basic_auth.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    from flaskblog.gallery.routes import gall
    from flaskblog.project.routes import proj

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(gall)
    app.register_blueprint(proj)

    with app.app_context():
        db.create_all()


    return app
