from flask import (render_template, url_for, flash, redirect,
                   request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db, basic_auth
from flask_basicauth import BasicAuth
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@basic_auth.required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, tags=form.tags.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.blog'))
    return render_template('create_post.html', title='New Post', form=form)


# posts = [
#     {
#         'author': 'JsonTyler',
#         'image': 'static/photos/introToBlogLaptop-min.jpg',
#         'title': 'Intro To Blog: JsonBytes',
#         'content': '''Hello and welcome to my blog dubbed JSONBYTES. Topics
#         discussed in this blog will be focused on 3 main topics:
#         - Programming
#         - Photography/Video Editing
#         - Traveling
#
#         To learn more about me or my projects feel free to check out my About Me.
#         ''',
#         'date_posted': 'June 18, 2019',
#         'tags': 'intro, blog'
#     },
#     {
#         'author': 'JsonTyler',
#         'image' : 'static/photos/bloggerson-min.jpg',
#         'title': 'Tkinter Woes: Bloggerson',
#         'content': '''Today, I want to talk about a plugin that I created for my blog using python's built in gui package Tkinter. In an effort to get up and going as fast and as organically as possible I opted for a static website for the time being versus a framework.
#
#         The upside to this was that it helped increase speed at start up being that I didnt have to waste time learning a new framework, nor did I have to waste time researching what fameworks may or may not be compatible with my website's hosting.
#
#         The downside to this was that as my blog gets bigger and bigger I am going to want to spend less time trying to figure out where to enter the different info for each post in the html code (ex: Title, Date, Topic, Content, and Image).
#
#         My solution to this apparent downside, so that a snow ball effect didn't happen down the road, was to create a GUI that would act as an interface to insert the data fields into a templated code block for me at the push of a button.
#
#         To dig further into the design of this plugin I took the first two weeks to read documentation which was found at https://tkdocs.com/. I read through the first eight or so sections of the tutorial which comprised of topics ranging from installation, concepts, basic widgets/advanced widgets, geometry managers, and menus. The third and final week I began by looking at other people's setups of tkinter apps to see what worked best. I decided on a object oriented
#         programming approach to both organize the code efficently and to practice the OOP concepts being that I needed some practice.
#
#         The widgets used were: Label, Entry, Button, Frame, and ScrolledText.
#
#         The user approach was to enter the Blog Entry's respective Title, Date, Topic, and Content into the respective entry fields. Then by clicking on the various ordered buttons it would both set and insert the above fields as well as
#         allow the user to choose an optional image to add to the then created blog post template.
#
#         I chose this approach because I wanted something that could scale in both size and complexity. One idea of mine originally had been to have the tkinter app communicate with the server on my website's hosting site...but I ultimately
#         decided that this would only complicate the application as well as to lengthen the creation time quite alot. I decided that it was just as easy to copy and paste the already filled out blog template from the test file onto the blog html
#         file being hosted.
#
#         The hardest part of the whole creation of the application, dubbed 'bloggerson' was to find a way to insert the set field's into an already entered template in the test file. I could open a file to insert text, but it would either
#         append it at the end...or it would overwrite the template code entirely.
#         To overcome this I added to each button's method some code that opened the test file and went through it line by line (and stored it), upon finding the keyword, I inserted the set text, then re-wrote the stored original template
#         line by line.
#
#         Some things to remember are to enter break line html elements to separate paragraphs, to only copy and not save the test file as to maintain the original template, and to store the images in the assets/css/img/blog filepath not the
#         local Downloads folder.
#
#         Future improvements I have for this project are to allow the user to attach other things than just images (ex: files, videos, sounds, and links) and to make the app overall more aestehically pleasing. I may also add some security to
#         check for validation on each data field's user entry.
#
#         Overall, my experience learning tkinter was very helpful in both building my foundation with Python and in creating a handy plugin to help automate my blog posts.
#
#         If you are interested in viewing the code you can check it out on my github page which is linked in the About section.
#
#         Thank you for reading.''',
#         'date_posted': 'July 1-22, 2019',
#         'tags': 'programming'
#     }
# ]
