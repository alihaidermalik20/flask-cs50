import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SPORTS = ["Basketball", "Football", "Tennis", "Swimming"]

@app.route('/')
def index():
    return render_template("index.html", sports=SPORTS)

# this route is taken when deregister button is clicked on registrant.html page
@app.route('/deregister', methods= ["POST"])
def deregister():
    # get the value of the button that was clicked which had a name of id. could also give this button name of deregister
    id = request.form.get("id")
    # if id isn't empty and some value was indeed selected, delete that id's row from our db
    if id:
        with sqlite3.connect("froshims.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM registrants WHERE id = ?", id)
            
    # redirect them to the path of registrants that goes to registrants.html page to show the new list
    return redirect("/registrants")

# if the register form is submitted from the index.html and it's valid, add it to your db and redirect to /registrant
# same as you do in /deregister and pass the displaying registrants in that one route
@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if sport == '':
        return render_template('/error.html', message='no sport selected')
    if not name:
        return render_template('/error.html', message='name not given')
    if sport not in SPORTS:
        return render_template('/error.html', message='sport not available')

    
    with sqlite3.connect("froshims.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))
        
    # after this it could either go to registrants.html page with render template where the registrants are going to be displayed
    # after you SELECT the all to be looped over on that page
    # but since you want ppl to see the registrants even if they add /registrants to their path and not go there only if they register
    # it's better to redirect them to /registrants so that ppl go to that path and be able to see the SELECT * on the page
    # from register, deregister and by simply typing /registrants as i won't give it methods POST condition 
    return redirect("/registrants")
        
# whenever /registrants is accessed with GET from deregister, register or by itself with /registrants, display registrants.html file
# and provide it with the SELECT * from our db
@app.route('/registrants')
def registrants():
    # then go the the registrants.html to show all registered ppl which are looped over because we provided the it with registrants
    with sqlite3.connect("froshims.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM registrants")
        registrants = cur.fetchall()
        return render_template("registrants.html", registrants=registrants)
