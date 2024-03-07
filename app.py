import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User 
from lib.property_repo import PropertyRepository
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from lib.property import Property
from lib.validator import * 
from datetime import datetime

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
    if 'user_id' not in session:
        return redirect('/login')
    else:
        return render_template('index.html')

@app.route("/login", methods=['GET'])
def login():
    if 'user_id' in session:
        return redirect('/')    
    else: 
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
    if Validator.check_spaces(username, password, email):
        return render_template("login.html", errors=Validator.space_error)
    # all these references validator.py class in lib folder 
    if Validator.check_password_invalid(password): 
        return render_template("login.html", errors=Validator.password_error)

    if not Validator.check_email(email):
        return render_template("login.html", errors=Validator.email_error)

    # we check if the user exists in our database
    user = repo.find_by_email(email)
    if user: 
        repo.check_password(password, email)
        # set the user ID and username in session
        session['user_id'] = user.id
        session['username'] = user.name
        return redirect("/") 
    
    # Finally if they're not in our database but they're given us valid info, we add 
    # them and start their session
    else: 
        repo.create(User(None, username, password, email))
        user = repo.find_by_email(email)
        # set the user ID in session 
        session['user_id'] = user.id
        session['username'] = user.name
        return redirect('/')

@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("user_id", None)
    session.clear()
    return redirect("/login")

# GET /places
# Returns the places page
# Try it:
#   ; open http://localhost:5000/places
@app.route('/places', methods=['GET'])
def get_places():
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.all()
    return render_template('/places/index.html', properties=properties)
    

# GET /places/new
# Returns the new place page
# Try it:
#   ; open http://localhost:5000/places/new
@app.route('/places/new', methods=['GET'])
def get_add_new_place():
    return render_template('places/new.html')

# GET /places/1
# Returns the page for a place by id
# Try it:
#   ; open http://localhost:5000/places/1
@app.route('/places/<int:id>', methods=['GET'])
def get_place_by_id(id):
    connection = get_flask_database_connection(app)
    property_repo = PropertyRepository(connection)
    property = property_repo.find(id)
    return render_template('places/show.html', property=property)

@app.route('/bookings/<int:id>', methods=['GET'])
def get_booking_by_id(id):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking = booking_repo.find(id)
    property_repo = PropertyRepository(connection)
    property = property_repo.find(booking.property_id)
    return render_template('bookings/show.html', booking=booking, property=property)

@app.route('/bookings', methods=['POST'])
def book_a_place():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    property_id = request.form['property_id']
    owner_id = request.form['owner_id']
    guest_id = session['user_id']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    name = request.form['name']
    booking = booking_repo.create(Booking(None, property_id, owner_id, guest_id, start_date, end_date, None, name))
    return redirect(f"/bookings/{booking.id}")


@app.route("/places", methods=['POST'])
def create_new_place_post():
    db_connect = get_flask_database_connection(app)
    repo = PropertyRepository(db_connect)
    name = request.form['name']
    description = request.form['desc']
    price = request.form['price']
    user_id = session['user_id']
    aval_start = request.form['aval_start']
    aval_end = request.form['aval_end']
    repo.create_space(Property(None, name, description, price, user_id, aval_start, aval_end))
    return redirect("/places")


@app.route("/requests", methods=['GET'])
def view_property_requests():
    db_connect = get_flask_database_connection(app)
    repo = BookingRepository(db_connect)
    rows = repo.all_by_owner_id(session["user_id"])
    bookings = repo.all_by_user_id(session["user_id"])
    return render_template('bookings/requests.html', rows=rows, bookings=bookings)

@app.route("/requests/<int:id>", methods=['GET'])
def get_individual_booking(id):
    db_connect = get_flask_database_connection(app)
    repo = BookingRepository(db_connect)
    user_repo = UserRepository(db_connect)
    property_repo = PropertyRepository(db_connect)
    booking = repo.find(id)
    user = user_repo.find(booking.guest_id)
    property_ = property_repo.find(booking.property_id)
    total_duration = booking.end_date - booking.starting_date
    total_price = total_duration.days * property_.price
    return render_template('bookings/single_request.html', booking=booking, property_=property_, user=user, price=total_price)

@app.route('/requests', methods=['POST'])
def confirm_deny():
    db_connect = get_flask_database_connection(app)
    repo = BookingRepository(db_connect)
    confirm = request.form.get("confirm")
    deny = request.form.get("deny")
    if confirm is not None: 
        repo.update(confirm)
    if deny is not None: 
        repo.delete(deny)
    return redirect("/requests")

@app.route('/your_properties', methods=['GET'])
def get_your_properties():
    db_connect = get_flask_database_connection(app)
    repo = PropertyRepository(db_connect)
    rows = repo.all_by_id(session['user_id'])
    return render_template('your_properties.html', rows=rows)
    
        

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
