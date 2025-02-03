# Learning_Flask
In this repository i will learn flask  with activities and projects

# Introducción a Flask

Flask es un microframework para Python que permite desarrollar aplicaciones web de manera sencilla y flexible. Es liviano y fácil de usar, ideal para proyectos pequeños y medianos.

## 🔹 Instalación
Antes de empezar, asegúrate de tener Python instalado en tu sistema. Luego, puedes instalar Flask con:

```sh
pip install flask
```

## 🔹 Hola Mundo en Flask
Crea un archivo `app.py` y escribe el siguiente código:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

Ejecuta la aplicación con:

```sh
python app.py
```

Luego, abre tu navegador y visita `http://127.0.0.1:5000/` para ver el mensaje `¡Hola, Flask!`.

## 🔹 Rutas y Parámetros
Puedes definir rutas con parámetros dinámicos:

```python
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'Hola, {nombre}!'
```

Ejemplo: Accediendo a `http://127.0.0.1:5000/saludo/Juan` mostrará `Hola, Juan!`.

## 🔹 Uso de JSON
Para devolver datos en formato JSON, usa `jsonify`:

```python
from flask import jsonify

@app.route('/api/datos')
def datos():
    return jsonify({"mensaje": "Hola, API"})
```

## 🔹 Ejecutando Flask en Modo Debug
Habilitar `debug=True` permite detectar cambios sin reiniciar el servidor:

```sh
flask --debug run
```

## 🔹 Conclusión
Flask es una excelente opción para construir aplicaciones web de manera rápida y sencilla. Es modular, fácil de aprender y compatible con muchas herramientas.

🚀 ¡Ahora puedes empezar a desarrollar con Flask!