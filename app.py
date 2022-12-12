from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from markupsafe import escape
import sqlite3

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():

    con = sqlite3.connect("app.db")

    cur = con.cursor()
    
    # execute the command to fetch all the data from the table emp
    res = cur.execute("SELECT * FROM users")
    
    # store all the fetched data in the ans variable
    ans = res.fetchall()
 
    print(ans)

    con.close()

    return render_template("layout.html")



@app.route("/login", methods=["POST", "GET"])
def login():

    

    return render_template("login.html")



@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
