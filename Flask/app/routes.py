from app import app, bcrypt
from flask import render_template, redirect, url_for, request, flash, session
from controllers.web_controller import create_new_user, get_user_by_email
from data.forms import RegistrationForm, LoginForm, PostForm
from data.models.models import Users, login_required, is_authenticated
from flask_login import login_user, current_user
from functools import wraps




@app.route('/', methods=["GET", "POST"])
def get_index():
    return render_template('base.html', status='Signed In' if is_authenticated() else 'Not Signed In')



@app.route("/restricted")
@login_required('restricted')
def restricted():
    return render_template('restricted.html', email=session['email'])




@app.route('/feed')
@login_required('restricted')
def get_feed():
    if 'email' in session:
        email = session['email']
    return render_template('feed.html', title='Feed')


@app.route('/profile')
@login_required('restricted')
def get_profile():
    return render_template('profile.html', title='Profile')


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        create_new_user(first_name, last_name, email, password)
        return redirect(url_for('sign_in'))
    return render_template('sign_up.html', form=form)


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_email(form.email.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = request.form['email']
            return redirect(url_for("get_feed"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("sign_in.html", title="Login", form=form)


@app.route('/test_profile')
@app.route('/test_profile.html')
def get_test_profile():
    return render_template('test_profile.html')


@app.route('/create_post', methods=["GET", "POST"])
def get_create_post():
    form = PostForm()
    return render_template('create_post.html', form=form)


@app.route("/signout")
def sign_out():
    session.clear()
    return redirect(url_for('get_index'))






"""  form = PostForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads' + filename)
        return redirect(url_for('create_post'))
"""
