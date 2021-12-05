from flask import request, jsonify, Blueprint
from datetime import datetime
from models.Transactions import Transactions
from app import db

bp = Blueprint('account', __name__, url_prefix = '/account')

@bp.route("/", methods = ['GET'])
def account():
  transactions = Transactions.query.all()
  transactionlist = [] 
  for transaction in transactions:
    transactionDetails = {
      'payer': transaction.payer,
      'points': transaction.points,
      'timestamp': transaction.timestamp
    }
    transactionlist.append(transactionDetails)
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
      message = {
        'status': 500,
        'message': 'Incorrect request',
        'request': req
      }
      return message
    message = {
      'status': 200,
      'message': 'Success',
      'request': req
    }
    return message

@bp.route("/spend", methods = ['GET'])
def spend():
  return "Success."