"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200
            

# Obtener un miembro específico por ID
@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    return jsonify({"message": "Miembro no encontrado"}), 404

# Agregar un nuevo miembro
@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    if not data.get("first_name") or not data.get("age") or not isinstance(data.get("lucky_numbers"), list):
        return jsonify({"message": "Datos incompletos o incorrectos"}), 400
    new_member = jackson_family.add_member(data)
    return jsonify(new_member), 201

# Eliminar un miembro por ID
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    if jackson_family.delete_member(id):
        return jsonify({"message": "Miembro eliminado correctamente"}), 200
    return jsonify({"message": "Miembro no encontrado"}), 404

# Actualizar datos de un miembro
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    updates = request.json
    updated_member = jackson_family.update_member(id, updates)
    if updated_member:
        return jsonify(updated_member), 200
    return jsonify({"message": "Miembro no encontrado"}), 404


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
