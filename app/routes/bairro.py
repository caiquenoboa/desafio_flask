from app import app
from flask import jsonify
from ..views import bairro

@app.route('/bairro', methods=['GET'])
def get_bairros():
    return bairro.get_bairros()

@app.route('/bairro/<id>', methods=['GET'])
def get_bairro(id):
   return bairro.get_bairro(id)

@app.route('/bairro', methods=['POST'])
def post_bairro():
   return bairro.post_bairro()

@app.route('/bairro/<id>', methods=['PUT'])
def update_bairro(id):
   return bairro.update_bairro(id)

@app.route('/bairro/<id>', methods=['DELETE'])
def delete_bairro(id):
   return bairro.delete_bairro(id)
