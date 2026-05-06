from flask import Flask, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


# Crear base de datos y tabla usuarios
def init_db():

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route('/')
def inicio():
    return "<h1>Servidor Flask funcionando</h1>"

@app.route('/registro', methods=['POST'])
def registro():

    datos = request.get_json()

    usuario = datos.get("user")
    password = datos.get("password")

    password_hash = generate_password_hash(password)

    try:

        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios (usuario, password)
            VALUES (?, ?)
        """, (usuario, password_hash))

        conn.commit()
        conn.close()

        return jsonify({
            "mensaje": "Usuario registrado correctamente"
        }), 201

    except sqlite3.IntegrityError:

        return jsonify({
            "error": "Ese usuario ya existe"
        }), 400
    
@app.route('/login', methods=['POST'])
def login():

    datos = request.get_json()

    user = datos.get("user")
    password = datos.get("password")

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT password
        FROM usuarios
        WHERE usuario = ?
    """, (user,))

    resultado = cursor.fetchone()

    conn.close()

    if resultado and check_password_hash(resultado[0], password):

        return jsonify({
            "mensaje": "Login exitoso"
        }), 200

    return jsonify({
        "error": "Credenciales incorrectas"
    }), 401


@app.route('/tareas', methods=['GET'])
def tareas():

    return """
    <h1>Bienvenido al Sistema de Tareas</h1>
    <p>API funcionando correctamente</p>
    """


if __name__ == "__main__":

    init_db()

    app.run(debug=True)