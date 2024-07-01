from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL, Optional

class LoginForm(FlaskForm):
    username = StringField('Gebruikersnaam', validators=[DataRequired()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    remember_me = BooleanField('Onthoud mij')
    submit = SubmitField('Inloggen')

class LeerlingForm(FlaskForm):
    naam = StringField('Naam', validators=[DataRequired(), Length(min=2, max=100)])
    afbeelding = StringField('Afbeelding URL', validators=[Optional(), URL()])
    submit = SubmitField('Opslaan')

class FeedbackForm(FlaskForm):
    lesdomein = SelectField('Lesdomein', choices=[
        ('rekenen', 'Rekenen'),
        ('taal', 'Taal'),
        ('spelling', 'Spelling'),
        ('lezen', 'Lezen'),
        ('creatief', 'Creatief'),
        ('wereldorientatie', 'Wereldoriëntatie')
    ], validators=[DataRequired()])
    concentratie = SelectField('Concentratie', choices=[
        ('goed', 'Goed'),
        ('voldoende', 'Voldoende'),
        ('onvoldoende', 'Onvoldoende')
    ], validators=[DataRequired()])
    werkhouding = SelectField('Werkhouding', choices=[
        ('goed', 'Goed'),
        ('voldoende', 'Voldoende'),
        ('onvoldoende', 'Onvoldoende')
    ], validators=[DataRequired()])
    doorzettingsvermogen = SelectField('Doorzettingsvermogen', choices=[
        ('goed', 'Goed'),
        ('voldoende', 'Voldoende'),
        ('onvoldoende', 'Onvoldoende')
    ], validators=[DataRequired()])
    submit = SubmitField('Feedback toevoegen')