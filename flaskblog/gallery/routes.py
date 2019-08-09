from flask import (render_template, url_for, flash, redirect,
                   request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db, basic_auth
from flask_basicauth import BasicAuth
from flaskblog.models import Gallery
from flaskblog.gallery.forms import GalleryForm
from flaskblog.users.utils import save_picture

gall = Blueprint('gall', __name__)

@gall.route("/gallery/new", methods=['GET', 'POST'])
@basic_auth.required
def new_image():
    form = GalleryForm()
    if form.validate_on_submit():
        gallerys = Gallery(filepath=form.filepath.data, location=form.location.data, caption=form.caption.data)
        db.session.add(gallerys)
        db.session.commit()
        flash('Your image has been uploaded!', 'success')
        return redirect(url_for('gall.gallery'))
    return render_template('create_gallery.html', title='New Image', form=form)

#new
gallery = ""

@gall.route("/gallery")
def gallery():
    gallery = Gallery.query.order_by(Gallery.location.desc())
    return render_template('gallery.html', images=images, title='Gallery', gallery=gallery)

# data
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
