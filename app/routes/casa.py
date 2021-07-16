from app import app
from flask import jsonify
from ..views import casa

@app.route('/casa', methods=['GET'])
def get_casas():
    return casa.get_casas()