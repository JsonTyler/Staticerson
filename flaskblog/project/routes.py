from flask import (render_template, url_for, flash, redirect,
                   request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db, basic_auth
from flask_basicauth import BasicAuth
from flaskblog.models import Project
from flaskblog.project.forms import ProjectForm
from flaskblog.users.utils import save_picture

proj = Blueprint('proj', __name__)

#new
project = ""

@proj.route("/project")
def project():
    project = Project.query.order_by(Project.title.desc())
    return render_template('projects.html', title='Projects', project=project)

# data