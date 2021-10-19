from flask import Flask  # From the flask package import the Flask class.


# Instantiate the Flask class into app (which is now an obj)
app = Flask(__name__)


@app.route("/")     # a decorator that maps a path to a view function.
def index():                                # A view function called index.
    return "<h1>Hello, world!<h1>"  # the return statement for index.


@app.route("/about")
def about_me():
    me = {
        "first_name": "Cameron",
        "last_name": "Campbell",
        "hobbies": "Video Games",
        "active": True
    }
    return me
