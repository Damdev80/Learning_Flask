from flask import Flask, request, jsonify





app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> ¡Bienvenido a Flask! </h1>"

@app.route('/hello')
def hello():
    return 'Hello, World'

#---
#Ejercicio 1

@app.route('/saludos/<nombre>')
def saludar(nombre):
    return f'Hola {nombre}'

##Ejercicio 2

@app.route('/suma/<int:n1>/<int:n2>')
def suma(n1,n2):
    resultado = n1 + n2
    return f"El resultado es {resultado}"

#Ejercicio 3
@app.route('/info',  methods=['GET'])
def infomation():
    show_header = request.headers
    show_conexion_sure = request.is_secure
    return jsonify({"headers": dict(show_header), "is_secure": show_conexion_sure})


    
    


if __name__ == "__main__":
    app.run(debug=True)
