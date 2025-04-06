# Formulario de contacto ULS
# Utilizando Flask como herramienta para desarrollo web y, esto para crear un formulario de contacto
# y almacenar los datos en una base de datos de prueba.
# Se utiliza el entorno virtual de Python como se indica en la actividad.
# Autor: Juan Pablo Sanchez Nieto
# Fecha: 2025-04-04

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Mover la inicialización de db fuera de la función

def crear_app():

    app = Flask(__name__)

    # Configuración de la conexión a Google Cloud SQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10771680:MHtwYjGmZh@sql10.freesqldatabase.com/sql10771680'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Inicializar db con la aplicación Flask

    # Modelo para la tabla de contactos
    class Contacto(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nombre = db.Column(db.String(80), nullable=False)
        email = db.Column(db.String(120), nullable=False)
        mensaje = db.Column(db.Text, nullable=False)

    @app.route('/')
    def index():
        return render_template('index.html')  # Página de inicio

    @app.route('/contacto')  # Ruta para el formulario de contacto
    def contacto():
        return render_template('contacto.html')

    @app.route('/submit_contacto', methods=['POST'])  # Función para manejar el envío del formulario
    def submit_contacto():
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        
        # Crear un nuevo contacto y agregarlo a la base de datos
        nuevo_contacto = Contacto(nombre=nombre, email=email, mensaje=mensaje)
        db.session.add(nuevo_contacto)
        db.session.commit()
        
        return redirect(url_for('mostrar_datos'))  # Redirigir a la página que muestra los datos

    @app.route('/mostrar_datos')  # Ruta para mostrar los datos almacenados
    def mostrar_datos():
        contactos = Contacto.query.all()  # Obtener todos los contactos
        return render_template('mostrar_datos.html', contactos=contactos)  # Pasar los contactos a la plantilla

    return app

if __name__ == '__main__':
    app = crear_app()  # Crear la aplicación Flask
    app.run(debug=True)  # Ejecutar la aplicación Flask