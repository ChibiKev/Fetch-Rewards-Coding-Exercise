from flask import Blueprint
# Flask is needed to build a web server using python.
# Request tells flask where we're getting our data and telling it to read it
# Jsonify provides us the form of our data

bp = Blueprint('add', __name__, url_prefix = '/')

@bp.route("/", methods = ['GET'])
def add():
  return "Success."