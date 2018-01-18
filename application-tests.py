import application
import unittest
from flask import json

# Mocks
catalog_data = '{"catalog": [{"id": "1",\
        "name": "soccer",\
        "items": [{"id": "1", "name": "soccer1", "description": "This is soccer 1. There is more soccer 1", "userid": "user1"},\
        {"id": "2", "name": "soccer2", "description": "This is soccer 2. There is more soccer 2", "userid": "user2"}\
        ]}, {"id": "2", "name": "tennis",\
            "items": [{"id": "1", "name": "tennis1", "description": "This is tennis 1. There is more tennis 1", "userid": "user1"}]}\
        ]}'

class AppTests(unittest.TestCase):
    def setUp(self):
        application.app.testing = True
        self.app = application.app.test_client()

    def test_catalog(self):
        cres = self.app.get('/catalog.json')
        catalog_orig = json.loads(catalog_data)
        catalog_res = json.loads(cres.data)
        self.assertDictEqual(catalog_res,catalog_orig)

if __name__ == '__main__':
    unittest.main()
