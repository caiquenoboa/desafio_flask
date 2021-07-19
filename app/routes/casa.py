from app import app
from flask import jsonify
from ..views import casa

@app.route('/casa', methods=['GET'])
def get_casas():
    return casa.get_casas()

@app.route('/casa/area/<id>', methods=['GET'])
def get_area(id):
   return casa.calcula_area(id)


@app.route('/casa/preco/<id>', methods=['GET'])
def get_preco(id):
   return casa.calcula_preco(id)

@app.route('/casa/<id>', methods=['GET'])
def get_casa(id):
   return casa.get_casa(id)

@app.route('/casa', methods=['POST'])
def post_casa():
   return casa.post_casa()

@app.route('/casa/<id>', methods=['PUT'])
def update_casa(id):
   return casa.update_casa(id)

@app.route('/casa/<id>', methods=['DELETE'])
def delete_casa(id):
   return casa.delete_casa(id)

@app.route('/casa/<id>/comodos', methods=['GET'])
def get_comodos_by_casa_id(id):
   return casa.get_comodos_by_casa_id(id)