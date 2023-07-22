from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'

# Create the students table if it does not exist
db.create_all()

# Endpoint to add a new student to the database
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data or 'grade' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    new_student = Student(name=data['name'], age=data['age'], grade=data['grade'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({'message': 'Student added successfully'}), 201

# Endpoint to retrieve all students from the database
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.__dict__ for student in students]), 200

# Endpoint to retrieve a specific student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    return jsonify(student.__dict__), 200

# Endpoint to update a specific student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data or 'grade' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    student.name = data['name']
    student.age = data['age']
    student.grade = data['grade']

    db.session.commit()

    return jsonify({'message': 'Student updated successfully'}), 200

# Endpoint to delete a specific student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({'message': 'Student deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
