from flask import Blueprint, render_template
from helpers import TmdbApiConnection

homepage = Blueprint('homepage', __name__, url_prefix='/')


@homepage.route('/')
def index():
    tmdb = TmdbApiConnection()
    return render_template('home.html', movies=tmdb.now_playing_movies, tvshows=tmdb.popular_tvseries)
