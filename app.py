from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm, LoginForm, PostForm
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config["SECRET KEY"] = ""


@app.route('/')
def get_index():
    return render_template('index.html')


@app.route('/feed')
def get_feed():
    return render_template('feed.html')


@app.route('/profile')
def get_profile():
    return render_template('profile.html')


@app.route('/test_profile')
@app.route('/test_profile.html')
def get_test_profile():
    return render_template('test_profile.html')


@app.route('/create_post')
def get_create_post():
    form = PostForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads' + filename)
        return redirect(url_for('create_post'))

    return render_template('create_post.html')


if __name__ == '__main__':
    app.run()
