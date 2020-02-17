from flask import redirect
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
