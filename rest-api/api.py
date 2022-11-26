import json
from flask import Flask, jsonify, request
import sqlite3
app = Flask(__name__)

# Criar a conexão a base de dados
def get_db_connection():
    conn = sqlite3.connect('../cambio/db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/cambios', methods=['GET'])
def index():
    try:
        cambios = []
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM cambioapp_cambios').fetchall()
        conn.close()
        # convert row objects to dictionary
        for i in posts:
            cambio = {}
            cambio["id"] = i["id"]
            cambio["valor"] = i["valor"]
            cambio["criado"] = i["criado"]
            cambio["editado"] = i["editado"]
            cambios.append(cambio)
    except:
        cambios = []
    return jsonify(cambios)


@app.route('/api/cambios/<id>', methods=['GET'])
def get_cambios_by_id(id):
    cambio = {}
    print(id)
    try:
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM cambioapp_cambios WHERE id = ?", 
                       (id,))
        i = cur.fetchone()
        
        # convert row objects to dictionary
        
        cambio["id"] = i["id"]
        cambio["valor"] = i["valor"]
        cambio["criado"] = i["criado"]
        cambio["editado"] = i["editado"]
        conn.close()
    except:
        cambio = []
    return cambio



@app.route('/api/cambios/add',  methods = ['POST'])
def insert_cambio():
    cambio = request.get_json()
    print(float(cambio['valor']))
    inserted_cambio = {}
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO cambioapp_cambios(valor, criado, editado) VALUES (?,2015-01-03,2015-01-03)", (float(cambio['valor']),))
        conn.commit()
        inserted_cambio = get_cambios_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_cambio



@app.route('/api/cambio/delete/<id>',  methods = ['DELETE'])
def api_delete_cambio(id):

    message = {}
    try:
        conn = get_db_connection()
        conn.execute("DELETE from cambioapp_cambios WHERE id = ?",(id,))
        conn.commit()
        message["status"] = "Cambio eliminado com sucesso"
    except:
        conn.rollback()
        message["status"] = "Nao eliminado"
    finally:
        conn.close()

    return message
    return jsonify(delete_user(user_id))



@app.route('/api/cambio/update',  methods = ['PUT'])
def update_cambio():
    updated_cambio = {}
    cambio = request.get_json()
    print(float(cambio['valor']))
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE cambioapp_cambios SET valor = ? WHERE id =?",  
                     (cambio["valor"],cambio["id"]))
        conn.commit()
        #return the user
        updated_cambio = get_cambios_by_id(cambio["id"])

    except:
        conn.rollback()
        updated_cambio = {}
    finally:
        conn.close()

    return updated_cambio


app.run()