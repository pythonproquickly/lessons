from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/dogs")
def dogs():
    return render_template("dogs.html")


@app.route("/passwordgenerator")
def passwordgenerator():
    content = []
    content.append("This is the heading")
    content.append(["Andy", "Fred", "Bill", "Harry"])
    content.append("The end")
    return render_template("passwordgenerator.html", content=content)


if __name__ == "__main__":
    app.run(debug=True)

