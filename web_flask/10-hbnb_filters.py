#!/usr/bin/python3
"""Starts a web application """
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """lists states and amenities from database"""
    z_states = storage.all(State)
    z_amenity = storage.all(Amenity)
    a_amenity = []
    all_states = []
    for key, value in z_states.items():
        all_states.append(value)
    for key, value in z_amenity.items():
        a_amenity.append(value)
    return render_template('10-hbnb_filters.html', all_states=all_states, a_amenity=a_amenity)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
