from flask import request, jsonify, Blueprint
from datetime import datetime
from models.Transactions import Transactions
from models.User import User
from app import db

bp = Blueprint('account', __name__, url_prefix = '/account')

@bp.route("/", methods = ['GET'])
def userProfile():
  user = User.query.get(1)
  if not user:
    print("No Vaild User: Creating User")
    user = User(points = 0, transaction = 0)
    db.session.add(user)
    db.session.commit()
  return "Current Points: " + str(user.points)

@bp.route("/checkUsers", methods = ['GET'])
def users():
  users = User.query.all()
  userlist = [] 
  for user in users:
    userlist.append(user.id)
  return jsonify(userlist)

@bp.route("/transactions", methods = ['GET'])
def transactionsList():
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
      user = User.query.get(1)
      if user:
        user.points += points
      else:
        print("No Vaild User: Creating User")
        user = User(points = points, transaction = 0)
      db.session.add(user)
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

@bp.route("/spend", methods = ['GET', 'POST'])
def spend():
  if request.method == 'GET':
    return "This is spend for transactions"
  elif request.method == 'POST':
    req = request.json
    try:
      requiredPoints = req['points']
    except:
      message = {
        'status': 500,
        'message': 'Incorrect request',
        'request': req
      }
      return message
    return req