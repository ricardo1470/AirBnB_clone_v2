#!/usr/bin/python3
from flask import Flask
""" script that starts a Flask web application
    Your web application must be
    listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB” """


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ display “Hello HBNB!” """
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display “HBNB!” """
    return ("HBNB")

if __name__ == '__main__':
    """ run server port 5000 """
    app.run(debug=True, port=5000, host='0.0.0.0')