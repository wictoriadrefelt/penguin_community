from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def get_index():
    return render_template('index.html')


@app.route('/logged_in')
def get_login_page():
    return render_template("logged_in.html")


if __name__ == '__main__':
    app.run()