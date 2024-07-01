import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'een_zeer_geheime_sleutel'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False