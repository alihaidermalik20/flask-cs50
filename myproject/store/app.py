from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import sqlite3

app = Flask(__name__)

# save cookies so your cart doesn't disappear
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
Session(app)

@app.route("/")
def index():
    with sqlite3.connect("store.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        books = cur.fetchall()
    return render_template("books.html", books = books)

@app.route('/cart', methods=["GET", "POST"])
def cart():
    if "cart" not in session:
        session["cart"] = []
    
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
        return redirect('/cart')

# works only with tuples not dictionaries for some reason
    tuple_cart_ids = tuple(session["cart"])

    with sqlite3.connect("store.db") as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM books WHERE (id) IN {tuple_cart_ids}")
        cart = cur.fetchall()
    return render_template("cart.html", cart=cart)