from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from . import db, limiter  # Adjusted import
from app.models import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')
