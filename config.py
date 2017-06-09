from decouple import config as Decouple
from dj_database_url import parse as db_url
import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Statement for enabling the development environment
    DEBUG = Decouple('DEBUG')
    # Statement for enabling the testing mode
    TESTING = Decouple('TESTING')

    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = Decouple(
        'DATABASE_URL',
        default='sqlite:///' + os.path.join(BASE_DIR, 'movie_center.db'),
        cast=db_url
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True
    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = Decouple('CSRF_SECRET_KEY')
    # Secret key for signing cookies
    SECRET_KEY = Decouple('SECRET_KEY')

    # Configuration for the Flask-Bcrypt Extension
    BCRYPT_LEVEL = Decouple('BCRYPT_LEVEL')

    # TMDB Movies Api Key
    TMDB_API_KEY = Decouple('TMDB_API_KEY')
