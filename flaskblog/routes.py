import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt, basic_auth
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_basicauth import BasicAuth

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

images = [
    {
        'filepath': 'static/photos/gallery/about_me.jpg',
        'location': 'Spokane, WA',
        'caption': 'Me in Spokane'
    },
    {
        'filepath': 'static/photos/gallery/cathedralTwo.jpg',
        'location': 'Spokane, WA',
        'caption': 'Cathedral in Spokane'
    },
    {
        'filepath': 'static/photos/gallery/christmasTexas.jpg',
        'location': 'Fort Worth, TX',
        'caption': 'Christmas Tree in Sundance Square'
    },
    {
        'filepath': 'static/photos/gallery/dunes.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Beach in Oregon'
    },
    {
        'filepath': 'static/photos/gallery/emergencyRoom.jpg',
        'location': 'Pasco, WA',
        'caption': 'Hospital in Pasco'
    },
    {
        'filepath': 'static/photos/gallery/FerrisWheelWashington.jpg',
        'location': 'Spokane, WA',
        'caption': 'Ferris Wheel in Spokane'
    },
    {
        'filepath': 'static/photos/gallery/flower.jpg',
        'location': 'The Dalles, OR',
        'caption': 'A flower found at Mayer State Park'
    },
    {
        'filepath': 'static/photos/gallery/fourthOfJulySmoke.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Fireworks for the 4th of July in on the Ocean.'
    },
    {
        'filepath': 'static/photos/gallery/gardensOne.jpg',
        'location': 'Spokane, WA',
        'caption': 'Botanical Gardens at Manito Park'
    },
    {
        'filepath': 'static/photos/gallery/gardensTwo.jpg',
        'location': 'Spokane, WA',
        'caption': 'Botanical Gardens at Manito Park'
    },
    {
        'filepath': 'static/photos/gallery/home_page2.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'River along campsite in Depoe Bay'
    },
    {
        'filepath': 'static/photos/gallery/lake.jpg',
        'location': 'Kennewick, WA',
        'caption': 'Sunset at park in Kennewick, WA'
    },
    {
        'filepath': 'static/photos/gallery/landing_page.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Beach in Depoe Bay, OR'
    },
    {
        'filepath': 'static/photos/gallery/me_at_beach.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Me on beach in Depoe Bay, OR'
    },
    {
        'filepath': 'static/photos/gallery/meGumWall.jpg',
        'location': 'Seattle, WA',
        'caption': 'Me at the Gum Wall in Seattle'
    },
    {
        'filepath': 'static/photos/gallery/meowtropolitan.jpg',
        'location': 'Seattle, WA',
        'caption': 'Seattle Meowtropolitan'
    },
    {
        'filepath': 'static/photos/gallery/middleOfNowhereLake.jpg',
        'location': 'Unknown',
        'caption': 'Middle of Nowhere Lake'
    },
    {
        'filepath': 'static/photos/gallery/oceanAgain.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Ocean in Depoe Bay'
    },
    {
        'filepath': 'static/photos/gallery/oceanYetAgain.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Ocean in Depoe Bay'
    },
    {
        'filepath': 'static/photos/gallery/oneTree.jpg',
        'location': 'Kennewick, WA',
        'caption': 'Tree at a park in Kennewick'
    },
    {
        'filepath': 'static/photos/gallery/oregonHotel.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'View from hotel on Oreogn coast'
    },
    {
        'filepath': 'static/photos/gallery/oregonHotelTwo.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Hotel on Oregon coast'
    },
    {
        'filepath': 'static/photos/gallery/OregonOutlookSign.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Outlook sign at hotel on Oregon coast'
    },
    {
        'filepath': 'static/photos/gallery/pathGreen.jpg',
        'location': 'Spokane, WA',
        'caption': 'A path at River Front Park'
    },
    {
        'filepath': 'static/photos/gallery/piano.jpg',
        'location': 'Spokane, WA',
        'caption': 'Inside the cathedral in Spokane'
    },
    {
        'filepath': 'static/photos/gallery/pierL.jpg',
        'location': 'Leavenworth, WA',
        'caption': 'The river in Leavenworth'
    },
    {
        'filepath': 'static/photos/gallery/publicMarket.jpg',
        'location': 'Seattle, WA',
        'caption': 'Public Market in Seattle'
    },
    {
        'filepath': 'static/photos/gallery/riverTwo.jpg',
        'location': 'Kennewick, WA',
        'caption': 'Columbia River in Kennewick'
    },
    {
        'filepath': 'static/photos/gallery/rocksAndOcean.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Beach on Oregon coast'
    },
    {
        'filepath': 'static/photos/gallery/seattle.jpg',
        'location': 'Seattle, WA',
        'caption': 'Street view in Seattle'
    },
    {
        'filepath': 'static/photos/gallery/spaceNeedle.jpg',
        'location': 'Seattle, WA',
        'caption': 'The Space Needle in Seattle'
    },
    {
        'filepath': 'static/photos/gallery/steph.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'My anniversary with my girlfriend on the Oregon coast'
    },
    {
        'filepath': 'static/photos/gallery/sunset_me.jpg',
        'location': 'Kennewick, WA',
        'caption': 'Me at a park in Kennewick watching the sunset'
    },
    {
        'filepath': 'static/photos/gallery/treeOutlook.jpg',
        'location': 'Newport, OR',
        'caption': 'Devils Punch Bowl outlook on Oregon Coast'
    },
    {
        'filepath': 'static/photos/gallery/trees.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Campground on the Oregon coast'
    },
    {
        'filepath': 'static/photos/gallery/view.jpg',
        'location': 'Fort Worth, TX',
        'caption': 'View from apartment overlooking the river in Texas'
    },
    {
        'filepath': 'static/photos/gallery/vines.jpg',
        'location': 'Seattle, WA',
        'caption': 'City center in Seattle'
    },
    {
        'filepath': 'static/photos/gallery/washingtonWaterPower.jpg',
        'location': 'Spokane, WA',
        'caption': 'Washington Water Power in Spokane'
    },
    {
        'filepath': 'static/photos/gallery/waves.jpg',
        'location': 'Depoe Bay, OR',
        'caption': 'Beach on the Oregon coast'
    }
]

blog=" "
gallery=" "

@app.route("/")
def index():
    return render_template('index.html', title="Home")

@app.route("/blog")
def blog():
    posts = Post.query.all()
    return render_template('blog.html', posts=posts, title="Blog", blog=blog)

@app.route("/gallery")
def gallery():
    return render_template('gallery.html', images=images, title='Gallery', gallery=gallery)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('blog'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog'))
    form = LoginForm()
    if form.validate_on_submit():
        # SAVE FOR ADDING ADMIN FUNCTIONALITY LATER
        # if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        #     flash('You have been logged in!', 'success')
        #     return redirect(url_for('blog'))
        # else:
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('blog'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('blog'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    # Resize image
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@basic_auth.required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, tags=form.tags.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('blog'))
    return render_template('create_post.html', title='New Post', form=form)
