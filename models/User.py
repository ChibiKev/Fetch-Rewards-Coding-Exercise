from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  points = db.Column(db.Integer(), unique=False, nullable=False)

  def __init__(self, points):
    self.points = points