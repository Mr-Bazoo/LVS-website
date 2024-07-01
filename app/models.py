from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Leerling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100), nullable=False)
    afbeelding = db.Column(db.String(200))
    feedback = db.relationship('Feedback', backref='leerling', lazy='dynamic')

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    leerling_id = db.Column(db.Integer, db.ForeignKey('leerling.id'), nullable=False)
    datum = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    lesdomein = db.Column(db.String(50), nullable=False)
    concentratie = db.Column(db.String(20), nullable=False)
    werkhouding = db.Column(db.String(20), nullable=False)
    doorzettingsvermogen = db.Column(db.String(20), nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))