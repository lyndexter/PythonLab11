from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from main.ua.lviv.iot.models.Cube import Cube
from main.ua.lviv.iot.models.Toy import Toy
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(user=SECRET["user"],
                                                                              password=SECRET["password"],
                                                                              host=SECRET["host"], port=SECRET["port"],
                                                                              db=SECRET["db"], )

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class BallEntity(Cube, db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    price_in_UAH = db.Column(db.FLOAT, unique=False)
    age_group = db.Column(db.Integer, unique=False)
    size = db.Column(db.String(20), unique=False)
    type_of_toy = db.Column(db.String(20), unique=False)
    color = db.Column(db.String(20), unique=False)
    filler = db.Column(db.String(20), unique=False)

    def __init__(self, color, filler, price_in_UAH, age_group, size):
        super().__init__(color, filler, price_in_UAH, age_group, size)


class BallEntitySchema(ma.Schema):
    class Meta:
        fields = ('color', 'filler', 'price_in_UAH', 'age_group', 'size')


ball_entity_schema = BallEntitySchema()
ball_entities_schema = BallEntitySchema(many=True)


@app.route("/ball", methods=["POST"])
def add_good_toy():
    ball_entity = BallEntity(request.json['color'], request.json['filler'], request.json['price_in_UAH'],
                             request.json['age_group'], request.json['size'])
    db.session.add(ball_entity)
    db.session.commit()
    return ball_entity_schema.jsonify(ball_entity)


@app.route("/ball", methods=["GET"])
def get_ball_entities():
    all_ball_entities = BallEntity.query.all()
    result = ball_entities_schema.dump(all_ball_entities)
    return jsonify({'good_toys_schema': result})


@app.route("/ball/<id>", methods=["GET"])
def get_ball_entity(id):
    ball_entity = BallEntity.query.get(id)
    if not ball_entity:
        abort(404)
    return ball_entity_schema.jsonify(ball_entity)


@app.route("/ball/<id>", methods=["PUT"])
def update_ball_entity(id):
    ball_entity = BallEntity.query.get(id)
    if not ball_entity:
        abort(404)
    old_ball_entity = copy.deepcopy(ball_entity)
    ball_entity.color = request.json['color']
    ball_entity.filler = request.json['filler']
    ball_entity.price_inUAH = request.json['price_inUAH']
    ball_entity.age_group = request.json['age_group']
    ball_entity.size = request.json['size']
    db.session.commit()
    return ball_entity_schema.jsonify(old_ball_entity)


@app.route("/ball/<id>", methods=["DELETE"])
def delete_ball_entity(id):
    ball_entity = BallEntity.query.get(id)
    if not ball_entity:
        abort(404)
    db.session.delete(ball_entity)
    db.session.commit()
    return ball_entity_schema.jsonify(ball_entity)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
