import flask

app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("home.html")


@app.route("/about")
def about():
    return flask.render_template("about.html")


@app.route("/andy")
def doit(a: int, b: int) -> float:
    """my function"""
    return a / b


if __name__ == "__main__":
    app.run(debug=True)
