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


@app.route('/states', strict_slashes=False)
def list_states():
    """lists states from database"""
    z_states = storage.all(State)
    all_states = []
    for key, value in z_states.items():
        all_states.append(value)
    return render_template('7-states_list.html', all_states=all_states)
    
   
@app.route('/states/<id>', strict_slashes=False)
def list_by_id(id):
    """display a HTML page if object id matches"""
    z_states = storage.all(State)
    all_states = []
    kid = []
    for key, value in z_states.items():
        all_states.append(value)
    for i in all_states:
            kid.append(i.id)
    return render_template('9-states.html', kid=kid, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
