from flask import (render_template, url_for, flash, redirect,
                   request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db, basic_auth
from flask_basicauth import BasicAuth
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
import sys

posts = Blueprint('posts', __name__)

@posts.route("/programming")
def topic_programming():
    p = request.args.get('p', 1, type=int)
    pp = 300
    stories = Post.query.order_by(Post.date_posted.asc()).paginate(p, pp)
    return render_template('topic_programming.html', stories=stories, title='Topic: Programming')

@posts.route("/frameworks")
def topic_frameworks():
    p = request.args.get('p', 1, type=int)
    pp = 300
    stories = Post.query.order_by(Post.date_posted.asc()).paginate(p, pp)
    return render_template('topic_frameworks.html', stories=stories, title='Topic: Frameworks')

@posts.route("/libraries")
def topic_libraries():
    p = request.args.get('p', 1, type=int)
    pp = 300
    stories = Post.query.order_by(Post.date_posted.asc()).paginate(p, pp)
    return render_template('topic_libraries.html', stories=stories, title='Topic: Libraries')

@posts.route("/algorithms")
def topic_algorithms():
    p = request.args.get('p', 1, type=int)
    pp = 300
    stories = Post.query.order_by(Post.date_posted.asc()).paginate(p, pp)
    return render_template('topic_algorithms.html', stories=stories, title='Topic: Algorithms')

@posts.route("/data")
def topic_data():
    p = request.args.get('p', 1, type=int)
    pp = 300
    stories = Post.query.order_by(Post.date_posted.asc()).paginate(p, pp)
    return render_template('topic_data.html', stories=stories, title='Topic: Data-Structures')

@posts.route("/projects")
def topic_projects():
    p = request.args.get('p', 1, type=int)
    pp = 300
    stories = Post.query.order_by(Post.date_posted.asc()).paginate(p, pp)
    return render_template('topic_projects.html', stories=stories, title='Topic: Projects')

@posts.route("/film")
def topic_film():
    p = request.args.get('p', 1, type=int)
    pp = 300
    stories = Post.query.order_by(Post.date_posted.asc()).paginate(p, pp)
    return render_template('topic_film.html', stories=stories, title='Topic: Film')

@posts.route("/thoughts")
def topic_thoughts():
    p = request.args.get('p', 1, type=int)
    pp = 300
    stories = Post.query.order_by(Post.date_posted.asc()).paginate(p, pp)
    return render_template('topic_thoughts.html', stories=stories, title='Topic: Thoughts')

@posts.route("/diy")
def topic_diy():
    p = request.args.get('p', 1, type=int)
    pp = 300
    stories = Post.query.order_by(Post.date_posted.asc()).paginate(p, pp)
    return render_template('topic_diy.html', stories=stories, title='Topic: DIY')
