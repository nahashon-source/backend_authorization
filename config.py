import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_really_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False