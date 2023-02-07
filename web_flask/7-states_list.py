#!/usr/bin/python3
"""Starts a web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """lists states from database
    Returns:
        HTML
    """
    z_states = storage.all(State)
    all_states = []
    for key, value in z_states.items():
        all_states.append(value)
    all_states = sorted(all_states)
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
