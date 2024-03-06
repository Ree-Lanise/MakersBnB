import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
# Create a new Flask app
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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
    # we establish a connection to the database 
    db_connect = get_flask_database_connection(app)
    repo = UserRepository(db_connect)
    
    # we grab the user input from the login page
    username = request.form['user']
    password = request.form['pass']
    email = request.form['email']
    # we make sure their input is valid
    if username == "" or password == "" or email == "":
        return render_template("login.html", errors="Username or Password Invalid")
    
    # we check if the user exists in our database
    user = repo.find_by_email(email)
    
    if user: 
        repo.check_password(password, email)
        # set the user ID in session
        session['user_id'] = user.id
        return redirect("/") 

    
    # Finally if they're not in our database but they're given us valid info, we add 
    # them and start their session
    else: 
        repo.create(User(None, username, password, email))
        user = repo.find_by_email(email)
        # set the user ID in session 
        session['user_id'] = user.id
        return redirect('/')

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
