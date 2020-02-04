from flask_wtf import FlaskForm
from flask_wtf.html5 import URLField
from wtforms import StringField, SubmitField
from flaskblog.models import Project
from wtforms.validators import DataRequired, url
from flask_uploads import UploadSet, IMAGES, configure_uploads


photos = UploadSet('photos', IMAGES)


class ProjectForm(FlaskForm):
    filepath = StringField('Filepath', validators=[DataRequired()])
    link = URLField('Url', validators=[url()])
    title = StringField('Title', validators=[DataRequired()])
    language = StringField('Technologies', validators=[DataRequired()])
    caption = StringField('Caption', validators=[DataRequired()])
    submit = SubmitField('Upload to Portfolio')
