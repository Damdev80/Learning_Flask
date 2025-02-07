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
    return jsonify({"headers": dict(show_header), "is_secure": show_conexion_sure}) #! Importante usar el dict() por que si no te dara error.

#Ejercicio 4
@app.route('/personalizado', methods=['GET', 'POST'])
def personalizado():
    my_cookie = make_response("Configurando cookie")
    my_cookie.set_cookie('Valor', ' Hola soy una cookie')
    cookie_value = request.cookies.get('Valor', 'No hay cookie configurada') #?El segundo valor  por si la cookie no tiene valor.
    return f'The value of my cookie is {cookie_value}',201
    
#Ejercicio 5
#___

#Ejercicio 6
@app.route('/api/datos', methods=['GET','POST'])
def api():
    info = {"nombre": "Flask", "Version": "2.1"}
    show_info = jsonify(info)
    return show_info
    

@app.route('/api/saludo/<string:nombre>', methods=['GET', 'POST'])
def saludos(nombre):
    return [
        {
            'Saludo': f'{nombre}' #? Otra forma de usar json!
        }
    ]
    

#Ejercicio 7
@app.route('/usuario', methods=['GET', 'POST'])
def get_data():
    prueba = request.method
    if prueba == 'GET':
        return "Lista de usuarios"
    elif prueba == 'POST':
        return "Usuario creado"
    else:
        return "Método no permitido", 405 #Código de estado HTTP 405 (Method Not Allowed)


if __name__ == "__main__":
    app.run(debug=True)
