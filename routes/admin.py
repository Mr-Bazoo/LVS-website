from flask import Blueprint, render_template, request, redirect, url_for
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import get_db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def admin():
    return render_template('admin.html')

@admin_bp.route('/add-student', methods=['POST'])
def add_student():
    name = request.form['name']
    avatar = request.form['avatar']
    db = get_db()
    db.execute('INSERT INTO students (name, avatar) VALUES (?, ?)', (name, avatar))
    db.commit()
    return redirect(url_for('admin.admin'))

@admin_bp.route('/students')
def students():
    db = get_db()
    students = db.execute('SELECT * FROM students').fetchall()
    return render_template('students.html', students=students)

@admin_bp.route('/edit-student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    db = get_db()
    if request.method == 'POST':
        name = request.form['name']
        avatar = request.form['avatar']
        db.execute('UPDATE students SET name = ?, avatar = ? WHERE id = ?', (name, avatar, id))
        db.commit()
        return redirect(url_for('admin.students'))
    student = db.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    return render_template('edit_student.html', student=student)