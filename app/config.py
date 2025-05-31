import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///instance/receitas.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
