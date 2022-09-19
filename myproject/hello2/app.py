from flask import Flask, render_template, request

app = Flask(__name__)

# simply going to index.html as home page


@app.route('/')
def index():
    return render_template("index.html")

# however, if the url route has /greet in the end, open the greet.html and provide it with variable name coming from value of the key name


@app.route('/greet')
def greet():
    # get the name from ?name= and if it's only /greet with no key value, name is World. won't work with ?name= path
    return render_template("greet.html", name=request.args.get("name", "World"))
