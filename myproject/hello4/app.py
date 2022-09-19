from crypt import methods
from unicodedata import name
from flask import Flask, render_template, request

app = Flask(__name__)

# one route for both get and post


@app.route('/', methods=["GET", "POST"])
def index():
    # if post method request submitted from the form submission with method post, go to greet page
    # and supply name with form.get not args.get as there are no args in the url with post, only with get
    # won't work if you go to url ?name=Ali
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "World"))
    return render_template("index.html")
