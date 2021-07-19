from app import db
from flask import json, request, jsonify
from .casa import delete_casa, get_information_casa
from ..models.bairro import Bairro, bairro_schema, bairros_schema
from ..models.casa import Casa, casas_schema, casa_schema
from ..models.comodo import Comodo, comodos_schema, comodo_schema


def get_bairros():
    bairros = Bairro.query.all()
    if bairros:
        result = bairros_schema.dump(bairros)
        return jsonify({'bairros': result})
    return jsonify({'message': 'nothing found'}), 404

def get_bairro(id):
    bairro = Bairro.query.get(id)
    if bairro:
        result = bairro_schema.dump(bairro)
        return jsonify({'bairro': result})
    return jsonify({'message': 'nothing found'}), 404

def post_bairro():
    name = request.json['name']
    preco_por_metro = request.json['preco_por_metro']
    bairro = Bairro(name, preco_por_metro)
    try:
        db.session.add(bairro)
        db.session.commit()
        result = bairro_schema.dump(bairro)
        return jsonify({'message': 'successfully registered', 'bairro': result}), 201
    except:
        return jsonify({'message': 'unable to create'}), 500

def update_bairro(id):
    name = request.json['name']
    preco_por_metro = request.json['preco_por_metro']
    bairro = Bairro.query.get(id)
    if not bairro:
        return jsonify({'message': 'nothing found'}), 404
    bairro.name = name
    bairro.preco_por_metro = preco_por_metro
    try:
        db.session.commit()
        result = bairro_schema.dump(bairro)
        return jsonify({'message': 'successfully updated', 'bairro': result}), 201
    except:
        return jsonify({'message': 'unable to update'}), 500

def delete_bairro(id):
    bairro = Bairro.query.get(id)
    if not bairro:
        return jsonify({'message': 'nothing found'}), 404
    casas = Casa.query.filter_by(bairro_id=bairro.id)
    for casa in casas:
        try:
            delete_casa(casa.id)
        except:
            return jsonify({'message': 'unable to delete'}), 500
    try:
        db.session.delete(bairro)
        db.session.commit()
        result = bairro_schema.dump(bairro)
        return jsonify({'message': 'successfully deleted', 'bairro': result})
    except:
        return jsonify({'message': 'unable to delete'}), 500


def get_casas_by_bairro(id, order):
    casas = Casa.query.filter_by(bairro_id=id).all()
    if not casas or len(casas) < 1:
        return jsonify({'message': 'nothing found'}), 404
    for casa in casas:
        get_information_casa(casa)
    
    if order == 'preco':
        casas.sort(key=lambda x:x.preco)
    elif order == 'num_comodos':
        casas.sort(key=lambda x:x.num_comodos)
    elif order == 'area':
        casas.sort(key=lambda x:x.area)
    
    result = casas_schema.dump(casas)
    return jsonify({'data': result})
