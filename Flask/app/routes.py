import codecs
import json
from app import app, bcrypt
from flask import jsonify, render_template, redirect, url_for, request, flash, session
from controllers.web_controller import create_new_user, get_user_by_email, create_new_post, get_all_posts, \
    get_users_by_first_name
from data.db import gridFS
from data.forms import RegistrationForm, LoginForm, PostForm
from data.models.models import Users, login_required, is_authenticated
from flask_login import login_user, current_user
from functools import wraps


@app.route('/search')
def get_search():
    return render_template('search.html')


@app.route('/process', methods=['POST'])
def post_process():
    user_search = request.form['name']
    db_search = get_users_by_first_name(user_search)
    result = [user.first_name.capitalize() for user in db_search]

    if user_search:
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
        return response  # jsonify({'name': new_name})

    return jsonify({'error': 'No penguins found.'})


@app.route('/feed')
@login_required('sign_in')
def get_feed():
    posts = get_all_posts()
    user_list = []
    photo_list = []
    description_list = []

    for post in posts:
        user_list.append(post.user)

    for post in posts:
        description_list.append(post.description)

    for post in posts:
        base64_data = codecs.encode(post.photo.read(), 'base64')
        image = base64_data.decode('utf-8')
        photo_list.append(image)

    zipped_list = zip(user_list, photo_list, description_list)

    return render_template('feed.html', title='Feed', zipped_list=zipped_list)


@app.route('/', methods=["GET", "POST"])
def get_index():
    return render_template('base.html', status='Signed In' if is_authenticated() else 'Not Signed In')


@app.route("/restricted")
def restricted():
    return render_template('restricted.html')


@app.route('/profile')
@login_required('sign_in')
def get_profile():
    return render_template('profile.html', title='Profile')


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    if is_authenticated():
        return redirect(url_for('get_feed'))

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
    if is_authenticated():
        return redirect(url_for('get_feed'))

    form = LoginForm()
    next_url = request.args.get('next')

    if form.validate_on_submit():
        user = get_user_by_email(form.email.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = request.form['email']
            return redirect(next_url) if next_url else redirect(url_for("get_feed"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("sign_in.html", title="Login", form=form)


@app.route('/test_profile')
@app.route('/test_profile.html')
def get_test_profile():
    return render_template('test_profile.html')


@app.route('/create_post', methods=["GET", "POST"])
@login_required('sign_in')
def get_create_post():
    form = PostForm()
    if form.validate_on_submit():
        email = session['email']
        description = form.description.data
        photo = form.file.data
        create_new_post(user, description, photo)
        flash("Congratulations, your post was successfully uploaded", "success")
    return render_template('create_post.html', form=form)


@app.route("/logged_out", methods=["GET", "POST"])
@login_required('restricted')
def logged_out():
    session.clear()
    return render_template('logged_out.html')


@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500


"""  form = PostForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads' + filename)
        return redirect(url_for('create_post'))
"""
