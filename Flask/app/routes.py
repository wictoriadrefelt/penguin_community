from app import app, bcrypt
from flask import render_template, redirect, url_for, request
from controllers.web_controller import create_new_user
from data.forms import RegistrationForm


@app.route('/')
def get_index():
    return render_template('sign_in.html')


@app.route('/feed')
def get_feed():
    return render_template('feed.html', title='Feed')


@app.route('/profile')
def get_profile():
    return render_template('profile.html', title='Profile')


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        create_new_user(first_name, last_name, email, hashed_password)
        return redirect(url_for('get_index'))
    return render_template('sign_up.html', form=form)


@app.route('/test_profile')
@app.route('/test_profile.html')
def get_test_profile():
    return render_template('test_profile.html')


@app.route('/create_post')
def get_create_post():
    return render_template('create_post.html')


"""  form = PostForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads' + filename)
        return redirect(url_for('create_post'))
"""
