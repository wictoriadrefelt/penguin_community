from app import app
from flask import render_template, request, redirect
from controllers.web_controller import create_new_user


@app.route('/')
def get_index():
    return render_template('sign_in.html')


@app.route('/feed')
def get_feed():
    return render_template('feed.html')


@app.route('/profile')
def get_profile():
    return render_template('profile.html')


@app.route('/sign_up')
def get_sign_up():
    return render_template('sign_up.html')


@app.route('/sign_up', methods=["POST"])
def post_sign_up():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    create_new_user(first_name, last_name, email, password)
    return render_template('sign_up.html')



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
