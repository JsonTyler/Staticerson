from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)



blog=" "
gallery=" "

# @main.route("/")
# def index():
#     return render_template('index.html', title="Home")

@main.route("/about")
def about():
    return render_template('about.html', title='About', about=about)

@main.route("/")
def blog():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    posts = Post.query.order_by(Post.date_posted.asc()).paginate(page, per_page)
    return render_template('blog.html', posts=posts, title="Blog", blog=blog)


