from flask import request, jsonify, Blueprint
from models.User import User
from app import db

bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route("/", methods = ['GET'])
def main():
  return "Welcome To The Fetch Rewards Coding Exercise API. Please Read the Readme."

@bp.route("/checkUsers", methods = ['GET'])
def users():
  users = User.query.all()
  userlist = [] 
  for user in users:
    userlist.append(user.id)
  return jsonify(userlist)