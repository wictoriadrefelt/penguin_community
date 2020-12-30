from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

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


if __name__ == '__main__':
    app.run()
