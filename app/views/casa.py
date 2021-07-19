from app import db
from flask import request, jsonify
from ..models.casa import Casa, casas_schema, casa_schema
from ..models.comodo import Comodo, comodos_schema
from ..models.bairro import Bairro


def calcule_area_util(casa):
    comodos = Comodo.query.filter_by(casa_id=casa.id).all()
    area_total = 0
    for comodo in comodos:
        area_total += comodo.calcula_area()
    return area_total

def calcule_preco_util(area, bairro_id):
    bairro = Bairro.query.get(bairro_id)
    return bairro.preco_por_metro * area

def calcule_num_comodos_util(casa):
    comodos = Comodo.query.filter_by(casa_id=casa.id).all()
    return len(comodos)

def get_information_casa(casa):
    casa.area = calcule_area_util(casa)
    casa.preco = calcule_preco_util(casa.area, casa.bairro_id)
    casa.num_comodos = calcule_num_comodos_util(casa)

def get_casas():
    casas = Casa.query.all()
    if casas:
        for casa in casas:
           get_information_casa(casa)
        result = casas_schema.dump(casas)
        return jsonify({'casas': result})
    return jsonify({'message': 'nothing found'}), 404

def get_casa(id):
    casa = Casa.query.get(id)
    if casa:
        get_information_casa(casa)
        result = casa_schema.dump(casa)
        return jsonify({'casa': result})
    return jsonify({'message': 'nothing found'}), 404

def calcula_area(id):
    casa = Casa.query.get(id)
    if not casa:
        return jsonify({'message': 'casa not found'}), 404
    area_total = calcule_area_util(casa)
    return jsonify({'area': area_total})

def calcula_preco(id):
    casa = Casa.query.get(id)
    if not casa:
        return jsonify({'message': 'casa not found'}), 404
    bairro = Bairro.query.get(casa.bairro_id)
    
    area_total = calcule_area_util(casa)
    
    preco = area_total * bairro.preco_por_metro
    return jsonify({'preco': preco})

def post_casa():
    name = request.json['name']
    bairro_id = request.json['bairro_id']
    casa = Casa(name, bairro_id)
    get_information_casa(casa)
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
    get_information_casa(casa)
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


def get_comodos_by_casa_id(id):
    comodos = Comodo.query.filter_by(casa_id=id).all()
    if not comodos or len(comodos) < 1:
        return jsonify({'message': 'nothing found'}), 404
    result = comodos_schema.dump(comodos)
    return jsonify({'comodos': result})