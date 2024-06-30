from flask import Blueprint, jsonify, request
from database import get_db
from datetime import date

api_bp = Blueprint('api', __name__)

@api_bp.route('/students')
def get_students():
    db = get_db()
    students = db.execute('SELECT * FROM students').fetchall()
    return jsonify([dict(student) for student in students])

@api_bp.route('/save-progress', methods=['POST'])
def save_progress():
    data = request.json
    db = get_db()
    db.execute('INSERT INTO progress (student_id, subject, domain, value, date) VALUES (?, ?, ?, ?, ?)',
               (data['studentId'], data['subject'], data['domain'], data['value'], date.today().isoformat()))
    db.commit()
    return jsonify({'message': 'Progress saved successfully'})