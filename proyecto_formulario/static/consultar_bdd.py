import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('database.db')

# Crear un cursor
cursor = conn.cursor()

# Realizar una consulta SELECT
cursor.execute('SELECT * FROM contactos')

# Obtener todos los resultados
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar la conexión
conn.close()