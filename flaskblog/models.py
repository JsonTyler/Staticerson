from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import Response, current_app
from flaskblog import db, login_manager, admin, basic_auth
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException
import enum

# login failed handler, from:
# https://computableverse.com/blog/flask-admin-using-basicauth
class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


# overwrite ModelView of flask_admin to restrict access to admin pageGallery
class ModelView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated. Refresh the page.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')"

class TagType(enum.Enum):
    programming = 'programming'
    frameworks='frameworks'
    libraries='libraries'
    algorithms='algorithms'
    data='data-structures'
    projects='projects'
    film='film'
    thoughts='thoughts'
    diy='diy'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    topic = db.Column(db.Enum(TagType, nullable=False))
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
   

admin.add_view(ModelView(Post, db.session))

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filepath = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    caption = db.Column(db.String(75), nullable=False)

    def __repr__(self):
        return f"Gallery('{self.filepath}', '{self.location}', '{self.caption}')"

admin.add_view(ModelView(Gallery, db.session))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filepath = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    caption = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Project('{self.filepath}', '{self.link}', '{self.title}', '{self.language}', '{self.caption}')"

admin.add_view(ModelView(Project, db.session))
