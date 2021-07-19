import unittest
import json
from app import app


class TestPingView(unittest.TestCase):
    def setUp(self):
        app2 = app.test_client()
        self.response = app2.get('/ping')
    
    def test_get(self):
        self.assertEqual(200, self.response.status_code)
    
    def test_json_string(self):
        self.assertEqual({'message': "pong"}, self.response.json)