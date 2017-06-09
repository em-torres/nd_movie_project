# Import flask and template operators
from flask import Flask
from views import homepage

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config.Config')

# Adding Views Blueprints to the app
app.register_blueprint(homepage)
