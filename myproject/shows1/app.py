from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    # every time something is typed in input, it's stored in request arguments under q
    q = request.args.get("q")
    # what will be passed in the sql query has to be in the format of (str,) with wildcards % before and after to select anything
    # that has that string in the title anywhere
    like = (f"%{q}%",)
    # if q isn't empty anymore
    if q:
        with sqlite3.connect("shows.db") as con:
            cur = con.cursor()
            cur.execute("SELECT title FROM shows WHERE title LIKE ? LIMIT 50", like)
            rows = cur.fetchall()
            shows = rows
    else:
        shows = []
    return render_template("search.html", shows=shows)
    # return jsonify(shows)