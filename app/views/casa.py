from app import db
from flask import request, jsonify
from ..models.casa import Casa, casas_schema, casa_schema
from ..models.comodo import Comodo, comodos_schema, comodo_schema


def get_casas():
    casas = Casa.query.all()
    if casas:
        result = casas_schema.dump(casas)
        return jsonify({'casas': result})
    return jsonify({'message': 'nothing found'}), 404

def get_casa(id):
    casa = Casa.query.get(id)
    if casa:
        result = casa_schema.dump(casa)
        return jsonify({'casa': result})
    return jsonify({'message': 'nothing found'}), 404

def calcula_area(id):
    casa = Casa.query.get(id)
    if not casa:
        return jsonify({'message': 'casa not found'}), 404
    comodos = Comodo.query.filter_by(casa_id=casa.id).all()
    area_total = 0
    for comodo in comodos:
        area_total += comodo.calcula_area()
    return jsonify({'data': area_total})

def post_casa():
    name = request.json['name']
    bairro_id = request.json['bairro_id']
    casa = Casa(name, bairro_id)
    try:
        db.session.add(casa)
        db.session.commit()
        result = casa_schema.dump(casa)
        return jsonify({'message': 'successfully registered', 'casa': result}), 201
    except:
        return jsonify({'message': 'unable to create'}), 500

def update_casa(id):
    name = request.json['name']
    bairro_id = request.json['bairro_id']
    casa = Casa.query.get(id)
    if not casa:
        return jsonify({'message': 'nothing found'}), 404
    casa.name = name
    casa.bairro_id = bairro_id
    try:
        db.session.commit()
        result = casa_schema.dump(casa)
        return jsonify({'message': 'successfully updated', 'casa': result}), 201
    except:
        return jsonify({'message': 'unable to update'}), 500

def delete_casa(id):
    casa = Casa.query.get(id)
    if not casa:
        return jsonify({'message': 'nothing found'}), 404
    comodos = Comodo.query.filter_by(casa_id=casa.id)
    for comodo in comodos:
        try:
            db.session.delete(comodo)
            db.session.commit()
        except:
            return jsonify({'message': 'unable to delete'}), 500
    try:
        db.session.delete(casa)
        db.session.commit()
        result = casa_schema.dump(casa)
        return jsonify({'message': 'successfully deleted', 'casa': result})
    except:
        return jsonify({'message': 'unable to delete'}), 500
