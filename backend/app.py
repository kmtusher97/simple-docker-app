from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from user_services import

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/userdb'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fullname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def __init__(self, email, fullname):
        self.email = email
        self.fullname = fullname


@app.before_first_request
def create_tables_in_database():
    print("ok")
    db.create_all()


@app.route('/')
def home():
    return '<h2>Home</h2>'


@app.route('/api/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_user_by_id():
    if request.method == 'GET':
        user_id = request.args.get('id')
        user_email = request.args.get('email')
        return jsonify('user1'), 200

    elif request.method == 'POST':

        return jsonify('user1'), 201

    elif request.method == 'PUT':
        return jsonify('user1'), 201

    elif request.method == 'DELETE':
        return jsonify('user1'), 201

    return 400


@app.route('/api/user/all/', methods=['GET'])
def get_user():
    return jsonify(['user1', 'user2']), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
