from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
import pymysql
pymysql.install_as_MySQLdb()

# initialize flask app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/userdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# initialize databse
db = SQLAlchemy(app)
# initialize marshmallow
ma = Marshmallow(app)

# model


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fullname = db.Column(db.String(80), nullable=False)

    def __init__(self, email, fullname):
        self.email = email
        self.fullname = fullname

    def __repr__(self):
        return '<User %r>' % self.email


class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'email', 'fullname')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.before_first_request
def create_tables_in_database():
    db.create_all()


# endpoints
@app.route('/')
def home():
    return '<h2>Home</h2>'


@app.route('/api/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_user_by_id():
    user_id = request.args.get('user_id')

    if request.method == 'GET':
        response = None

        if user_id:
            user = User.query.get(user_id)
            response = user_schema.dump(user)

        else:
            all_users = User.query.all()
            response = users_schema.dump(all_users)

        return jsonify(response), 200

    elif request.method == 'POST':
        email = request.json['email']
        fullname = request.json['fullname']

        new_user = User(email, fullname)

        db.session.add(new_user)
        db.session.commit()

        return user_schema.jsonify(new_user), 201

    elif request.method == 'PUT':
        email = request.json['email']
        fullname = request.json['fullname']

        user = User.query.get(user_id)
        user.email = email
        user.fullname = fullname
        db.session.commit()

        return user_schema.jsonify(user), 200

    elif request.method == 'DELETE':
        user = User.query.get(user_id)
        
        if user:
            db.session.delete(user)
            db.session.commit()
        
        return user_schema.jsonify(user), 204

    return 400


# run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
