from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def get_index():
    return render_template('index.html')


@app.route('/feed')
def get_feed():
    return render_template('feed.html')


@app.route('/profile')
def get_profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run()
