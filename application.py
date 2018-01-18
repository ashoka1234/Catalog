from flask import Flask, request, make_response
import json

# set the project root directory as the static folder
app = Flask(__name__)

# Mocks
catalog_data = '{"catalog": [{"id": "1",\
        "name": "soccer",\
        "items": [{"id": "1", "name": "soccer1", "description": "This is soccer 1. There is more soccer 1", "userid": "user1"},\
        {"id": "2", "name": "soccer2", "description": "This is soccer 2. There is more soccer 2", "userid": "user2"}\
        ]}, {"id": "2", "name": "tennis",\
            "items": [{"id": "1", "name": "tennis1", "description": "This is tennis 1. There is more tennis 1", "userid": "user1"}]}\
        ]}'

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/catalog.json')
def catalog():
    return catalog_data

@app.route('/catalog/<category>/edit/<name>', methods = ['PUT'])
def edit(category,name):
    res = make_response()
    res.status_code = 201
    res.headers['location'] = '/catalog/<category>/edit/<name>'
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
