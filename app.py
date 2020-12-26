from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def get_index():
    return render_template('base.html')

@app.route("/profile")
def get_profile():
    return render_template("profile.html")




if __name__ == '__main__':
    app.run()