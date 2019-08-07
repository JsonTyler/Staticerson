from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flaskblog.models import Post
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    submit = SubmitField('Post')
