from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# creating an empty dictionary to store registered users in
REGISTRANTS = {}

SPORTS = ['basketball', 'football', 'tennis', 'swimming']


@app.route('/')
def index():
    return render_template("index.html", sports=SPORTS)


@app.route('/register', methods=['POST'])
def register():

    # form submission on index page takes you to /register with POST method and inside the form, whatever element
    # has name of "name" will be taken by request.form.get and stored as variable name in this function
    name = request.form.get("name")
    # if the name is empty, it will take you to error page and pass the variable message as name not provided
    if not name:
        return render_template("error.html", message='Name not provided')

    sport = request.form.get("sport")
    # if the default empty option is selected or sport isn't in the list of SPORTS take to error page with different messages
    if sport == '':
        return render_template("error.html", message='Sport not selected')

    if sport not in SPORTS:
        return render_template("error.html", message='Sport not available')

    # save the users name and sport in the dictionary with key name and value the sport they selected
    REGISTRANTS[name] = sport

# if all passes, it shows you the registered page and provides the page with dictionary registrants to loop over and show
# all registered users and their sports on this page
    return render_template("registered.html", registrants=REGISTRANTS)
