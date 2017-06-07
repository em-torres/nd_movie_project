from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__, url_prefix='/')


@homepage.route('/')
def index():
    return render_template('home.html')
