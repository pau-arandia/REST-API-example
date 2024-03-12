from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

#############################################################################################
# 1. Run this in cmd to create environment variables
#    (this needs to be done every time the cmd is closed):
#
#       set FLASK_APP=application.py
#       set FLASK_ENV=development
#
#    Then run:
#       flask run --debug
#
#    This will return the port where the website is running.
#    Debug mode shows an interactive debugger whenever a page raises an exception, 
#    and restarts the server whenever you make changes to the code. 
#    You can leave it running and just reload the browser page.
#
# 2. To create the database, run the 'create_sql_db.py' file from the cmd on the 
#    same route that this file is stored by executing this command on the cmd:
#
#       python create_sql_db.py
#
#    This only needs to be done if the database does not exist.
#############################################################################################

# Flask setup: application instance
app = Flask(__name__)

# Configure the SQLite database and call it 'data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.app_context().push()

# Connect to the database
db = SQLAlchemy(app)

# Connect to the database with ORM (object relational mapper) by defining all the things we want
# to store in the database as models = create a class

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)

    # Wrapper method for representation
    # 'self' refers to the object, so we can grab the object's attribute by passing self.attribute_name
    def __repr__(self):
        return f"{self.name} - {self.description}"


# METHOD: Create endpoint
@app.route('/')
def index():
    return 'Hello!'


# METHOD: Create app to store drinks:
@app.route('/drinks')
def get_drinks():

    # Get all drinks in JSON format
    drinks = Drink.query.all()

    # Serialize the output
    output = []

    for drink in drinks:
        drink_data = {"name" : drink.name, 
                      "description" : drink.description}
        
        output.append(drink_data)

    return {"drinks" : output}


# METHOD: Create app to add ID to each drink:
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)

    return {"name" : drink.name,
            "description" : drink.description}


# METHOD: Adding a new drink to the database (POST)
@app.route('/drinks', methods=['POST'])
def add_drink():

    # Get the request data to get the drink attributes
    # 'request.json' is the way to get the JSON data from a request
    drink = Drink(name = request.json["name"],
                  description = request.json["description"])
    
    # Add the query to the database
    db.session.add(drink)
    db.session.commit()

    print('Successfully added')
    return {"id" : f"Drink with ID = {drink.id} was added to the database"}


# METHOD: Delete a drink from the database (DELETE)
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):

    drink = Drink.query.get(id)

    if drink is None:
        return {"error" : "404 Not found"}, 404

    db.session.delete(drink)
    db.session.commit()

    return {"message" : f"Drink with ID = {id} was deleted from the database"}