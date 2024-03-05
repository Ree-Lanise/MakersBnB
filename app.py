import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /
# Returns the homepage
# Try it:
#   ; open http://localhost:5000
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def login_post():
    username = request.form['user']
    password = request.form['pass']
    if username == "" or password == "":
        return render_template("login.html", errors="Username or Password Invalid")
    else:
        return redirect("/")

# GET /places
# Returns the places page
# Try it:
#   ; open http://localhost:5000/places
@app.route('/places', methods=['GET'])
def get_places():
    return render_template('places/index.html')

# GET /places/new
# Returns the new place page
# Try it:
#   ; open http://localhost:5000/places/new
@app.route('/places/new', methods=['GET'])
def get_add_new_place():
    return render_template('places/new.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
