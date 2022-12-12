from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from markupsafe import escape
from werkzeug.security import check_password_hash, generate_password_hash
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

# connection for SQL
connection = sqlite3.connect('app.db', check_same_thread=False)
cursor = connection.cursor()

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/login", methods=["POST", "GET"])
def login():
    # Forget any user_id
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return ("<p>invalid username</p>")
        # Ensure password was submitted
        elif not request.form.get("password"):
            return ("<p>invalid password</p>")
        # Query database for username
        rows = cursor.execute(f"SELECT * FROM users WHERE username IS '{request.form.get('username')}'").fetchall()
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0][2], request.form.get("password")):
            return ("<p>invalid username and/or password</p>")
        # Remember which user has logged in
        session["user_id"] = rows[0][0]
        # Redirect user to home page
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return ("<p>must provide username</p>")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return ("<p>must provide password</p>")

        elif request.form.get("password") != request.form.get("confirmation"):
            return ("<p>both passwords must be the same</p>")

        # checks if username is already in data
        elif (cursor.execute(f"SELECT username FROM users WHERE username IS '{request.form.get('username')}'").fetchall() != []):
            return ("<p>username is not availible</p>")


        cursor.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (request.form.get("username"), generate_password_hash(
            request.form.get("password"), method='pbkdf2:sha256', salt_length=8)))

        connection.commit()

    """Register user"""
    return render_template("./register.html")


@app.route('/')
def index():

    # con = sqlite3.connect("app.db")

    # cur = con.cursor()

    # # execute the command to fetch all the data from the table emp
    # res = cur.execute("SELECT * FROM users")

    # # store all the fetched data in the ans variable
    # ans = res.fetchall()

    # print(ans)

    # con.close()

    return render_template("layout.html")


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
