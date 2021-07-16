from app import db
from flask import request, jsonify
from ..models.casa import Casa, casas_schema, casa_schema


def get_casas():
    casas = Casa.query.all()
    if casas:
        result = casas_schema.dump(casas)
        return jsonify({'data': result})
    return jsonify({'message': 'nothing found'}), 404