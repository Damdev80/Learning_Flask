from flask import Flask, request, jsonify, make_response 





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

#Ejercicio 4
@app.route('/personalizado', methods=['GET', 'POST'])
def personalizado():
    my_cookie = make_response("Configurando cookie")
    my_cookie.set_cookie('Valor', ' Hola soy una cookie')
    return my_cookie,201
    
    


if __name__ == "__main__":
    app.run(debug=True)
