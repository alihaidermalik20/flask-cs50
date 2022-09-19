from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ["Basketball", "Tennis", "Soccer", "Swimming"]

# index.html should have the list of SPORTS as they will be used to dynamically add options with a loop to the page
# changing the list in one place automatically changes the options on the page and wherever else SPORTS has been used


@app.route('/')
def index():
    return render_template("index.html", sports=SPORTS)

# form on index.html goes to /register using POST method if submitted. have to specify method POST as GET is the default


@app.route('/register', methods=["POST"])
def register():
    # if a name value isn't provided in the text input field or a sport is added into DOM or selected the empty option, take to failure page
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    return render_template("success.html")
