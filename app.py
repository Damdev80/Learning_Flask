from flask import Flask


app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> ¡Bienvenido a Flask! </h1>"

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/saludos/<nombre>')
def saludar(nombre):
    return f'Hola {nombre}'

@app.route('/suma/<int:n1>/<int:n2>')
def suma(n1,n2):
    resultado = n1 + n2
    return f"El resultado es {resultado}"

if __name__ == "__main__":
    app.run(debug=True)
