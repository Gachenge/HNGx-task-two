from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Gachenge:root12345@Gachenge.mysql.pythonanywhere-services.com/Gachenge$Persons'
app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

with app.app_context():
    db.create_all()

@app.route('/api', methods=['GET', 'POST'])
def create_person():
    if request.method == 'GET':
        people = Person.query.all()
        people_list = [{"id": person.id, "name": person.name} for person in people]
        return jsonify(people_list)

    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        if not isinstance(name, str):
            return jsonify({"Error": "Name must be a string"}), 400
        existing_person = Person.query.filter_by(name=name).first()
        if existing_person:
            return jsonify({"Error": "Name is already registered"}), 400
        person = Person(name=name)
        db.session.add(person)
        db.session.commit()
        return jsonify({"message": "Person added successfully"}), 201


@app.route('/api/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_person(user_id):
    person = Person.query.get(user_id)
    if not person:
        return jsonify({"Error": "Person not found"}), 404

    if request.method == 'GET':
        return jsonify({"id": person.id, "name": person.name})

    if request.method == 'PUT':
        data = request.get_json()
        new_name = data.get('name')
        if not isinstance(new_name, str):
            return jsonify({"Error": "Name must be a string"}), 400
        person.name = new_name
        db.session.commit()
        return jsonify({"message": "Person updated successfully"})

    if request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successfully"})
