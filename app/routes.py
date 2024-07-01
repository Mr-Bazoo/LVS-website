from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, limiter
from app.models import Leerling, Feedback, User
from app.forms import LeerlingForm, FeedbackForm, LoginForm
from datetime import datetime

@app.route('/')
@app.route('/home')
def home():
    search = request.args.get('search')
    page = request.args.get('page', 1, type=int)
    if search:
        leerlingen = Leerling.query.filter(Leerling.naam.contains(search)).paginate(page=page, per_page=10)
    else:
        leerlingen = Leerling.query.paginate(page=page, per_page=10)
    return render_template('home.html', leerlingen=leerlingen, search=search)

@app.route('/leerling/<int:leerling_id>')
def leerling_detail(leerling_id):
    leerling = Leerling.query.get_or_404(leerling_id)
    feedback_form = FeedbackForm()
    return render_template('leerling_detail.html', leerling=leerling, form=feedback_form)

@app.route('/leerling/<int:leerling_id>/add_feedback', methods=['POST'])
@login_required
def add_feedback(leerling_id):
    leerling = Leerling.query.get_or_404(leerling_id)
    form = FeedbackForm()
    if form.validate_on_submit():
        new_feedback = Feedback(
            leerling_id=leerling.id,
            datum=datetime.now().date(),
            lesdomein=form.lesdomein.data,
            concentratie=form.concentratie.data,
            werkhouding=form.werkhouding.data,
            doorzettingsvermogen=form.doorzettingsvermogen.data
        )
        db.session.add(new_feedback)
        db.session.commit()
        flash('Feedback toegevoegd.', 'success')
    return redirect(url_for('leerling_detail', leerling_id=leerling.id))

@app.route('/add_leerling', methods=['GET', 'POST'])
@login_required
def add_leerling():
    form = LeerlingForm()
    if form.validate_on_submit():
        leerling = Leerling(naam=form.naam.data, afbeelding=form)