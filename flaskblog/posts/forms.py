from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from flaskblog.models import Post
from wtforms.validators import DataRequired
from flaskblog.models import TagType

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    tags = SelectField('Topic', choices=['programming', 'frameworks', 'libraries', 'algorithms', 'data-structures', 'Projects',
                       'film', 'thoughts', 'diy'])
    submit = SubmitField('Post')

    
