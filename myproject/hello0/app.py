from flask import Flask, render_template, request

# opening this file, which is defined by __name__, with Flask and can use it as app
app = Flask(__name__)

# whenever the route goes to home page indicated by /


@app.route('/')
def index():
    # docs show request.args.get has first parameter of key to get and second parameter of default
    # so get from the request the argument under key name or whatever comes after /?name=
    # and if there's no /?name= but just the home page ending with /, name is World and not /?name="World"
    name = request.args.get("name", "World")
    # render name variable to the index.html page
    return render_template("index.html", name=name)
