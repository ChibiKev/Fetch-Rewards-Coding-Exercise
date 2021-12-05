from flask_sqlalchemy import SQLAlchemy
from app import db

class Transactions(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(100), unique=False, nullable=False)

  def __init__(self, content):
    self.content = content