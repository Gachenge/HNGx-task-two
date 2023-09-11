from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Gachenge:root12345@Gachenge.mysql.pythonanywhere-services.com/Gachenge$Persons'
db = SQLAlchemy()
db.init_app(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


@app.route('/api', methods=['GET', 'POST'])
def addPerson():
    if request.method == 'POST':
        name = request.args.get('name')
        if not isinstance(name, str):
            return jsonify({"Error": "Name must be string"})
        person = Person(name=name)
        db.session.add(person)
        db.session.commit()
        res = f"{name} added successfully"
        return jsonify(res)
    people = Person.query.all()
    peop = [{"id": person.id, "name": person.name} for person in people]
    return jsonify(peop)


@app.route('/api/<int:user_id>')
def getPerson(user_id):
    person = Person.query.filter_by(id=user_id).first()
    if person:
        return jsonify({"id": person.id, "name": person.name})
    return jsonify({"Error": "Person not found"}), 404


@app.route('/api/<int:user_id>', methods=['GET', 'PUT'])
def updPerson(user_id):
    person = Person.query.filter_by(id=user_id).first()
    if person:
        nami = request.args.get('name')
        if not isinstance(nami, str):
            return jsonify({"Error": "Name must be string"})
        person.name = nami
        db.session.commit()
        return jsonify({"id": person.id, "name": person.name})
    return jsonify({"Error": "Person not found"}), 404


@app.route('/api/<int:user_id>', methods=['GET', 'DELETE'])
def delPerson(user_id):
    person = Person.query.filter_by(id=user_id).first()
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({"Success": "deleted"})
    return jsonify({"Error": "Person not found"}), 404


@app.route('/api/<string:name>', methods=['GET'])
def get_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person:
        return jsonify({"id": person.id, "name": person.name})
    return jsonify({"Error": "Person not found"}), 404


with app.app_context():
    db.create_all()
app.run()
