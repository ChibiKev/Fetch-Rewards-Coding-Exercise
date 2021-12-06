from flask import request, jsonify, Blueprint
from sqlalchemy import asc
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
    user = User(points = 0, transaction = 1)
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
  transactionList = [] 
  for transaction in transactions:
    transactionDetails = {
      'payer': transaction.payer,
      'points': transaction.points,
      'timestamp': transaction.timestamp
    }
    transactionList.append(transactionDetails)
  return jsonify(transactionList)

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
        user = User(points = points, transaction = 1)
      db.session.add(user)
      db.session.commit()
      message = {
        'status': 200,
        'message': 'Success',
        'request': req
      }
    except:
      message = {
        'status': 500,
        'message': 'Incorrect request',
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
      user = User.query.get(1)
      if not user:
        print("No Vaild User: Creating User")
        user = User(points = 0, transaction = 1)
        db.session.add(user)
        db.session.commit()
      if requiredPoints > user.points:
        message = {
          'status': 500,
          'message': 'Insufficient Funds',
          'request': req
        }
      else:
        transactionValue = user.transaction
        transactionList = []
        transactions = Transactions.query.filter(Transactions.id > transactionValue).order_by(asc(Transactions.timestamp)).all()
        for transaction in transactions:
          found = next((index for (index, d) in enumerate(transactionList) if d['payer'] == transaction.payer), None)
          if transaction.points < requiredPoints:
            requiredPoints -= transaction.points
            if found == None:
              transactionDetails = {
                'payer': transaction.payer,
                'points': 0 - transaction.points,
              }
              transactionList.append(transactionDetails)
            else:
              transactionList[found]["points"] -= transaction.points
          else:
            difference = transaction.points - requiredPoints
            transactionValue = transaction.id
            if found == None:
              transactionDetails = {
                'payer': transaction.payer,
                'points': 0 - requiredPoints,
              }
              transactionList.append(transactionDetails)
            else:
              transactionList[found]["points"] -= requiredPoints
            break
        return jsonify(transactionList)
    except:
      message = {
        'status': 500,
        'message': 'Incorrect request',
        'request': req
      }
    return message