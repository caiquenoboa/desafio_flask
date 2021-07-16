from app import app
from flask import jsonify

@app.route('/ping', methods=['GET'])
def root():
    return jsonify({'message': 'pong'})