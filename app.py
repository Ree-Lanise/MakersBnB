import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.property_repo import PropertyRepository


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


# /places/view_spaces
# Lists current spaces
# Try it:
#   ; open http://localhost:5000/places/view_spaces
@app.route('/places/view_spaces')
def view_spaces():
    return render_template('/places/view_spaces.html')




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
