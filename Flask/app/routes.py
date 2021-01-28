import codecs
import json

from app import app, bcrypt
from flask import jsonify, render_template, redirect, url_for, request, flash, session
from controllers.web_controller import create_new_user, get_user_by_email, create_new_post, get_all_posts, \
    get_users_by_first_or_last_name, get_user_by_id, get_post_by_post_id, delete_post_by_id, create_new_comment, \
    get_posts_by_user_id, add_friend, add_fish_to_post
from data.db import gridFS
from data.forms import RegistrationForm, LoginForm, PostForm, CommentForm
from data.models.models import Users, login_required, is_authenticated
from flask_login import login_user, current_user
from functools import wraps


@app.route('/post/<post_id>/post_fish', methods=["POST"])
def fish_post(post_id):
    email = session['email']
    add_fish_to_post(post_id, email)
    flash('One fish added to this post!', 'success')
    return redirect(url_for('get_feed'))


@app.route('/post/<post_id>/post_delete', methods=["POST"])
def delete_post(post_id):
    delete_post_by_id(post_id)
    flash('The post is now deleted', 'success')
    return redirect(url_for('get_feed'))


@app.route('/post/<post_id>/follow', methods=["POST"])
def follow(user_id):
    delete_post_by_id(post_id)
    flash('The post is now deleted', 'success')
    return redirect(url_for('get_feed'))


@app.route('/post/<post_id>/comment_post',  methods=["POST"])
def post_comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        email = session['email']
        comment = form.comment.data
        create_new_comment(email, comment, post_id)
        return redirect(url_for('get_post', post_id=post_id))


@app.route('/post/<post_id>',  methods=["GET", "POST"])
def get_post(post_id):
    form = CommentForm()  # uses for send comment

    post = get_post_by_post_id(post_id)

    comments_list = []
    profile_picture_list = []

    for comment in post.comments:
        comments_list.append(comment)

    for comment in post.comments:
        base64_data_3 = codecs.encode(comment.user.profile_picture.read(), 'base64')
        p_picture_2 = base64_data_3.decode('utf-8')
        profile_picture_list.append(p_picture_2)

    base64_data = codecs.encode(post.photo.read(), 'base64')
    image = base64_data.decode('utf-8')

    base64_data_2 = codecs.encode(post.user.profile_picture.read(), 'base64')
    p_picture = base64_data_2.decode('utf-8')

    zipped_list = zip(comments_list, profile_picture_list)

    return render_template('post.html', post=post, image=image, p_picture=p_picture,
                           form=form, zipped_list=zipped_list)


@app.route('/search')
def get_search():
    return render_template('search.html')


@app.route('/process', methods=['POST'])
def post_process():
    user_input = request.form['name']
    result = get_users_by_first_or_last_name(user_input)

    if user_input:
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
    post_list = []
    profile_picture_list = []

    for post in posts:
        user_list.append(post.user)

    for post in posts:
        base64_data = codecs.encode(post.photo.read(), 'base64')
        image = base64_data.decode('utf-8')
        photo_list.append(image)

    for post in posts:
        post_list.append(post)

    for post in posts:
        base64_data = codecs.encode(post.user.profile_picture.read(), 'base64')
        p_picture = base64_data.decode('utf-8')
        profile_picture_list.append(p_picture)

    zipped_list = zip(user_list, photo_list, post_list, profile_picture_list)

    return render_template('feed.html', title='Feed', zipped_list=zipped_list)


@app.route('/', methods=["GET", "POST"])
def get_index():
    return render_template('base.html', status='Signed In' if is_authenticated() else 'Not Signed In')


@app.route("/restricted")
def restricted():
    return render_template('restricted.html')


@app.route('/profile/<user_id>',  methods=["GET", "POST"])
@login_required('sign_in')

def get_others_profile(user_id):

    user = get_user_by_id(user_id)
    posts = get_posts_by_user_id(user.id)

    user_list = []
    photo_list = []
    post_list = []
    profile_picture_list = []

    for post in posts:
        user_list.append(post.user)

    for post in posts:
        base64_data = codecs.encode(post.photo.read(), 'base64')
        image = base64_data.decode('utf-8')
        photo_list.append(image)

    for post in posts:
        post_list.append(post)

    for post in posts:
        base64_data = codecs.encode(post.user.profile_picture.read(), 'base64')
        p_picture = base64_data.decode('utf-8')
        profile_picture_list.append(p_picture)

    zipped_list = zip(user_list, photo_list, post_list, profile_picture_list)

    return render_template('profile.html', title='Profile', zipped_list=zipped_list)


@app.route('/profile',  methods=["GET", "POST"])
@login_required('sign_in')
def get_profile():

    email = session['email']
    user = get_user_by_email(email)
    user_id = user.id
    return redirect(url_for("get_others_profile", user_id=user_id))




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
        profile_picture = form.file.data
        create_new_user(first_name, last_name, email, password, profile_picture)
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
        create_new_post(email, description, photo)
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
