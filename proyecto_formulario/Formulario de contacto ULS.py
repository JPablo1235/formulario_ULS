from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from crear_bdd import crear_base_datos  # Importa la función desde crear_bdd.py

app = Flask(__name__)

# Llama a la función para crear la base de datos al iniciar la aplicación
crear_base_datos()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')  # Asegúrate de que este archivo exista

@app.route('/submit_contacto', methods=['POST'])
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

@app.route('/mostrar_datos')
def mostrar_datos():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contactos')
    contactos = cursor.fetchall()
    conn.close()
    return render_template('mostrar_datos.html', contactos=contactos)

if __name__ == '__main__':
    app.run(debug=True)