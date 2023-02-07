#!/usr/bin/python3

"""
a script that starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """display hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """display the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_is_fun(text=None):
    """display the text variable"""
    if text is None:
        text = "is cool"
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_integer(n):
    """displays a number"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_int(n):
    """displays a number"""
    return render_template("5-number.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
