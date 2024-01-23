import flask
import json

app = flask.Flask(__name__)

@app.route('/')
def index():
    data={
        "name":"ram",
        "age":20,
    }
    return json.dumps(data)

@app.route('/users')
def users():
    udata=[
        {"id":1,"name":"ram","age":20},
        {"id":2,"name":"shyam","age":21},
        {"id":3,"name":"hari","age":22},
    ]
    return json.dumps(udata)