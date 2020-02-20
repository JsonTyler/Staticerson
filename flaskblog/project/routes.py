from flask import (render_template, url_for, flash, redirect,
                   request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db, basic_auth
from flask_basicauth import BasicAuth
from flaskblog.models import Project
from flaskblog.project.forms import ProjectForm

proj = Blueprint('proj', __name__)

project = ""

@proj.route("/", methods=["POST", "GET"])
def project(): 
    project = Project.query.order_by(Project.title.desc())
    projects = Project.query.all()
    return render_template('test.html', title='Projects', project=project)
