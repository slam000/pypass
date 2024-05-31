# database.py
import sqlite3

def inicializar_db():
    conn = sqlite3.connect('gestor_contraseñas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contraseñas
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 servicio TEXT NOT NULL, 
                 nombre_usuario TEXT NOT NULL, 
                 contraseña TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def agregar_contraseña(servicio, nombre_usuario, contraseña):
    conn = sqlite3.connect('gestor_contraseñas.db')
    c = conn.cursor()
    c.execute('INSERT INTO contraseñas (servicio, nombre_usuario, contraseña) VALUES (?, ?, ?)', 
              (servicio, nombre_usuario, contraseña))
    conn.commit()
    conn.close()

def obtener_contraseñas():
    conn = sqlite3.connect('gestor_contraseñas.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contraseñas')
    rows = c.fetchall()
    conn.close()
    return rows

def eliminar_contraseña(id):
    conn = sqlite3.connect('gestor_contraseñas.db')
    c = conn.cursor()
    c.execute('DELETE FROM contraseñas WHERE id=?', (id,))
    conn.commit()
    conn.close()
