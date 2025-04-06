
# Formulario de contacto ULS
# Utilizando Flask como herramienta para desarrollo web y SQLite para la BDD, esto para crear un formulario de contacto
# y almacenar los datos en una base de datos de prueba SQLite.
# Se utiliza el entorno virtual de Python como se indica en la actividad.
# Autor: Juan Pablo Sanchez Nieto
# Fecha: 2025-04-04



from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from crear_bdd import crear_base_datos  # Importa la función desde crear_bdd.py

def crear_app():

    app = Flask(__name__)

    # Funcion para crear la base de datos y la tabla si no existen
    crear_base_datos()

    @app.route('/')
    def index():
        return render_template('index.html') # Página de inicio

    @app.route('/contacto') # Ruta para el formulario de contacto
    def contacto():
        return render_template('contacto.html')

    @app.route('/submit_contacto', methods=['POST']) # Funcion para manejar el envío del formulario
    def submit_contacto():
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        
        # Conectar a la base de datos y agregar el nuevo contacto
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contactos (nombre, email, mensaje) VALUES (?, ?, ?)', (nombre, email, mensaje))
        conn.commit()
        conn.close()
        
        return redirect(url_for('mostrar_datos'))  # Redirigir a la página que muestra los datos

    @app.route('/mostrar_datos') # Ruta para mostrar los datos almacenados
    def mostrar_datos():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contactos') # Consulta para obtener todos los contactos
        contactos = cursor.fetchall()
        conn.close()
        return render_template('mostrar_datos.html', contactos=contactos)
    return app

if __name__ == '__main__':
    app = crear_app() # Crear la aplicación Flask para correrla en Render.com
    app.run()  # Ejecutar la aplicación Flask