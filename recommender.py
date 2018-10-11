from flask import Flask
from flask import request
app = Flask(__name__)

users = []
companies = []


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        context = request.get_json()
        users.append(context['name'])
        print(users)
        return '', 200