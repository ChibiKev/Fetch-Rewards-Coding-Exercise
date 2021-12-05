from flask_sqlalchemy import SQLAlchemy
from app import db

class Transactions(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  payer = db.Column(db.String(100), unique=False, nullable=False)
  points = db.Column(db.Integer(), unique=False, nullable=False)
  timestamp = db.Column(db.DateTime(), unique=False, nullable=False)

  def __init__(self, payer, points, timestamp):
    self.payer = payer
    self.points = points
    self.timestamp = timestamp