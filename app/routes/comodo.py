from app import app
from ..views import comodo

@app.route('/comodo', methods=['GET'])
def get_comodos():
    return comodo.get_comodos()

@app.route('/comodo/<id>', methods=['GET'])
def get_comodo(id):
   return comodo.get_comodo(id)

@app.route('/comodo/area/<id>', methods=['GET'])
def calcula_area(id):
   return comodo.calcule_area(id)

@app.route('/comodo', methods=['POST'])
def post_comodo():
   return comodo.post_comodo()

@app.route('/comodo/<id>', methods=['PUT'])
def update_comodo(id):
   return comodo.update_comodo(id)

@app.route('/comodo/<id>', methods=['DELETE'])
def delete_comodo(id):
   return comodo.delete_comodo(id)