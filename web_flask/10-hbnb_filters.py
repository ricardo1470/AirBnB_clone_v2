#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__, template_folder='templates')


@app.route('/hbnb_filters', strict_slashes=False)
def states_list(id='0'):
    """ Display HTML page with list of states """
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values(), id=id)


@app.teardown_appcontext
def remove_session(response_or_exc):
    """ Remove the current SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    """ run server port 5000 """
    app.run(debug=True, port=5000, host='0.0.0.0')
