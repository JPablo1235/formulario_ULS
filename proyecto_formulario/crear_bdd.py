# crear_bdd.py
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