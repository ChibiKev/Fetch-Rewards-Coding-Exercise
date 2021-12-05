from flask import request, jsonify, Blueprint
from datetime import datetime
from models.Transactions import Transactions
from app import db
# Flask is needed to build a web server using python.
# Request tells flask where we're getting our data and telling it to read it
# Jsonify provides us the form of our data

bp = Blueprint('account', __name__, url_prefix = '/account')

@bp.route("/", methods = ['GET'])
def account():
  transactions = Transactions.query.all()
  transactionlist = [] 
  for transaction in transactions:
    payer = transaction.payer
    points = transaction.points
    timestamp = transaction.timestamp
    transactionlist.append([payer, points, timestamp])
  return jsonify(transactionlist)

@bp.route("/add", methods = ['GET', 'POST'])
def addTransactions():
  if request.method == 'GET':
    return "This is add for transactions"
  elif request.method == 'POST':
    req = request.json  
    try:
      payer = req['payer']
      points = req['points']
      timestamp = datetime.strptime(req['timestamp'],"%Y-%m-%dT%H:%M:%SZ")
      transaction = Transactions(payer = payer, points = points, timestamp = timestamp)
      db.session.add(transaction)
      db.session.commit()
    except: 
      return "Incorrect request"
    return req

@bp.route("/spend", methods = ['GET'])
def spend():
  return "Success."