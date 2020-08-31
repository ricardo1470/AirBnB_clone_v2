#!/usr/bin/python3
from flask import Flask
from flask import render_template
""" script that starts a Flask web application
    Your web application must be
    listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB” 
    /c/<text>: display “C ” followed by the value
    of the text variable
    /python/(<text>): display “Python ”,
    followed by the value of the text variable.
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer
    /number_odd_or_even/<n>: display a HTML page only if n is an integer """


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ display “Hello HBNB!” """
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display “HBNB!” """
    return ("HBNB")

@app.route('/c/<text>/', strict_slashes=False)
def c(text = "value"):
    """ display “C ” followed by the value of the text variable """
    return ('C {}'.format(text.replace("_", " ")))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def python(text = "is cool"):
    """ display “Python ”, followed by the value of the text variable """
    return ('Python {}'.format(text.replace("_", " ")))


@app.route('/number', strict_slashes=False)
@app.route('/number/<int:n>/', strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer """
    return ('{} is a number'.format(n))

@app.route('/number_template', strict_slashes=False)
@app.route('/number_template/<int:n>/', strict_slashes=False)
def number_template(n):
    """ display “n is a number” only if n is an integer """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>/', strict_slashes=False)
def number_odd_or_even(n):
    """  display a HTML page only if n is an integer """
    return render_template('6-number_odd_or_even.html', number_odd_or_even=n)

if __name__ == '__main__':
    """ run server port 5000 """
    app.run(debug=True, port=5000, host='0.0.0.0')