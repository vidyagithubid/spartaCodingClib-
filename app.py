from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('Your mongoDB Atlas URL here')
db = client.dbhomework


## HTML 
@app.route('/')
def homework():
    return render_template('index.html')


# POST API
@app.route('/order', methods=['POST'])
def save_order():
# Fill this out!

    return jsonify({'result': 'success'})


# Read API
@app.route('/order', methods=['GET'])
def view_orders():
# Fill this out!!
    return jsonify({'result': 'success', 'orders': 'orders'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)