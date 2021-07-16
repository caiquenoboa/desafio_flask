from app import db
from flask import request, jsonify
from ..models.comodo import Comodo, comodos_schema, comodo_schema


def get_comodos():
    comodos = Comodo.query.all()
    if comodos:
        result = comodos_schema.dump(comodos)
        return jsonify({'comodos': result})
    return jsonify({'message': 'nothing found'}), 404

def get_comodo(id):
    comodo = Comodo.query.get(id)
    if not comodo:
        return jsonify({'message': 'comodo not found'}), 404
    result = comodo_schema.dump(comodo)
    return jsonify({'comodo': result})

def calcule_area(id):
    comodo = Comodo.query.get(id)
    if not comodo:
        return jsonify({'message': 'comodo not found'}), 404
    return jsonify({'area' : comodo.calcula_area()})

def post_comodo():
    name = request.json['name']
    largura = request.json['largura']
    comprimento = request.json['comprimento']
    casa_id = request.json['casa_id']
    comodo = Comodo(largura, comprimento, name, casa_id)
    try:
        db.session.add(comodo)
        db.session.commit()
        result = comodo_schema.dump(comodo)
        return jsonify({'message': 'successfully registered', 'comodo': result}), 201
    except:
        return jsonify({'message': 'unable to create'}), 500

def update_comodo(id):
    name = request.json['name']
    largura = request.json['largura']
    comprimento = request.json['comprimento']
    casa_id = request.json['casa_id']
    comodo = Comodo.query.get(id)
    try:
        comodo.name = name
        comodo.largura = largura
        comodo.comprimento = comprimento
        comodo.casa_id = casa_id
        db.session.commit()
        result = comodo_schema.dump(comodo)
        return jsonify({'message': 'successfully updated', 'comodo': result}), 201
    except:
        return jsonify({'message': 'unable to update'}), 500

def delete_comodo(id):
    comodo = Comodo.query.get(id)
    if not comodo:
        return jsonify({'message': 'nothing found'}), 404
    
    try:
        db.session.delete(comodo)
        db.session.commit()
        result = comodo_schema.dump(comodo)
        return jsonify({'message': 'successfully deleted', 'comodo': result})
    except:
        return jsonify({'message': 'unable to delete'}), 500