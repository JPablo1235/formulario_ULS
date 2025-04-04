
# Este script crea una base de datos SQLite y una tabla para almacenar los datos del formulario de contacto.
# La base de datos se crea en un archivo llamado 'database.db' y la tabla se llama 'contactos'.
# La tabla tiene cuatro columnas: id (clave primaria), nombre, email y mensaje.
# Se crea una funcion para crear la base de datos y la tabla si no existen, esta se llama en el script principal.

import sqlite3

def crear_base_datos(): 
    # Conectar a la base de datos (se creará si no existe)
    conn = sqlite3.connect('database.db')

    # Crear un cursor
    cursor = conn.cursor()

    # Crear una tabla
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        mensaje TEXT NOT NULL
    )
    ''')

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()