from flask import Flask, request, jsonify, make_response 
import datetime




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
@app.before_request
def registrar_acceso():
    # Obtener el método HTTP y la URL solicitada
    metodo = request.method
    url = request.url

    # Obtener la fecha y hora actual
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Registrar la información en el archivo log.txt
    with open("log.txt", "a") as archivo_log:
        archivo_log.write(f"[{ahora}] Método: {metodo}, URL: {url}\n")

# Hook after_request: Agrega el encabezado X-Powered-By a todas las respuestas
@app.after_request
def agregar_encabezado(response):
    # Agregar el encabezado personalizado
    response.headers['X-Powered-By'] = 'Flask'
    return response

# Ruta de prueba
@app.route('/')
def inicio():
    return "¡Bienvenido a la aplicación Flask!"

# Ruta de prueba adicional
@app.route('/test')
def test():
    return "Esta es una ruta de prueba."  

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
        return "Método no permitido", 405 #?Código de estado HTTP 405 (Method Not Allowed)
    

@app.route('/app_notas/<int:nota>', methods=['GET', 'POST', 'DELETE'])
def app_notas(Nueva_nota, Nota_Eliminada,nota):
    Validacion  = request.method
    if  Validacion == 'GET':
        return [
            {
                'Notas': 5.0
            }
        ]
    elif Validacion == 'POST':
        return [
            {
                Nueva_nota: 3.5
            }
        ]
    elif Validacion == 'DELETE':
        return [
            {
                Nota_Eliminada: Nueva_nota
            }
        ]
    elif Validacion == 'GET' and Validacion == 'int' :
        return[
            {
                'Tu nota': nota
            }
        ]
    else:
        return 'Metodo no admitido.', 405
    
        
        
        


if __name__ == "__main__":
    app.run(debug=True)
