#!/usr/bin/python3
"""Starts a web application """
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """lists states and amenities from database"""
    z_states = storage.all(State)
    z_amenity = storage.all(Amenity)
    z_place = storage.all(Place)
    a_amenity = []
    all_states = []
    a_place = []
    for key, value in z_states.items():
        all_states.append(value)
    for key, value in z_amenity.items():
        a_amenity.append(value)
    for key, value in z_place.items():
        a_place.append(value)
    
    return render_template('10-hbnb_filters.html', all_states=all_states, a_amenity=a_amenity, a_place=a_place)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
