from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')  # 'mongo' is the name of the MongoDB service in Docker Compose
db = client['mydatabase']  # Name of your MongoDB database
collection = db['users']  # Collection name to store user data


@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form
    name = data['name']
    email = data['email']
    user_data = {'name': name, 'email': email}
    collection.insert_one(user_data)
    return jsonify({'message': 'Data stored successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
