from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> ¡Bienvenido a Flask! </h1>"

