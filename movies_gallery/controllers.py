from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
# from werkzeug import check_password_hash, generate_password_hash
# from movies_gallery import db
# from movies_gallery.forms import LoginForm
# from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
hello = Blueprint('hello', __name__, url_prefix='/')

# Set the route and accepted methods
# @mod_auth.route('/signin/', methods=['GET', 'POST'])
# def signin():
#     # If sign in form is submitted
#     form = LoginForm(request.form)
#
#     # Verify the sign in form
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and check_password_hash(user.password, form.password.data):
#             session['user_id'] = user.id
#             flash('Welcome %s' % user.name)
#             return redirect(url_for('auth.home'))
#         flash('Wrong email or password', 'error-message')
#     return render_template("auth/signin.html", form=form)


@mod_auth.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("home.html")
