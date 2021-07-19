import unittest
import json
from app import app

class TestCasaViewGetAll(unittest.TestCase):
    def setUp(self):
        app2 = app.test_client()
        self.response = app2.get('/casa')
    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

class TestCasaViewGet(unittest.TestCase):
    def setUp(self):
        app2 = app.test_client()
        self.response = app2.get('/casa/2')
    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)
    
    def test_json_string(self):
        self.assertEqual({'casa': {'area': 60, 'bairro_id': 2, 'id': 2, 'name': 'casa agua verde 1', 'num_comodos': 4, 'preco': 600}}, self.response.json)


class TestCasaViewGetError(unittest.TestCase):
    def setUp(self):
        app2 = app.test_client()
        self.response = app2.get('/casa/1')
    
    def test_get(self):
        self.assertEqual(404, self.response.status_code)
    
    def test_json_string(self):
        self.assertEqual({'message': 'nothing found'}, self.response.json)