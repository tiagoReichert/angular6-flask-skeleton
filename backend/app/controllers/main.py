from flask import Blueprint, jsonify
from app.models import Version, User, db
main = Blueprint('main', __name__)


@main.route('/version')
def version():
    return Version.query.one().version


@main.route('/users')
def users():
    return jsonify([u.serialize for u in User.query.all()])
