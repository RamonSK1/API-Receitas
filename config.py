import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///receitas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False