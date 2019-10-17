import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my-precious"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or f"sqlite:///{os.path.join(basedir, 'studentApp.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False