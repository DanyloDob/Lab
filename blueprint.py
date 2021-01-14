from flask import Blueprint, jsonify, request
#from flask_jwt import jwt_required, current_identity

import db_utils
from middlewares import only_admin_access, only_target_user_access_or_admin

from models import User, Tickets, Session

from schemas import (

    UserData,
    UserToCreate,
    UserToUpdate,
    TicketData,
    TicketToCreate,
    StatusResponse
)

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route("/user", methods=["POST"])

def create_user():
    user_data = UserToCreate().load(request.json)
    user = db_utils.create_entry(User, **user_data)
    return jsonify(UserData().dump(user))


@api_blueprint.route("/user/<int:user_id>", methods=["GET"])

def get_user_by_id(user_id):
    user = db_utils.get_entry_by_idd(User, user_id)
    return jsonify(UserData().dump(user))


@api_blueprint.route("/user/<int:user_id>", methods=["PUT"])

def update_user(user_id):
    session = Session()
    user_data = UserToUpdate().load(request.json)
    user = db_utils.get_entry_by_idd(User, user_id)
    db_utils.update_entry(user, **user_data)
    session.commit()
    return jsonify(StatusResponse().dump({"code": 200}))

@api_blueprint.route("/user/<int:user_id>", methods=["DELETE"])

def delete_user(user_id):
    db_utils.delete_entry(User, user_id)
    return jsonify(StatusResponse().dump({"code": 200}))


@api_blueprint.route("/ticketss", methods=["POST"])

def create_ticket():
    ticket_data = TicketToCreate().load(request.json)
    ticket = db_utils.create_entry(Tickets, **ticket_data)
    return jsonify(ticket_data().dump(ticket))


@api_blueprint.route("/ticketss", methods=["GET"])

def list_of_Tickets():
    ticket_data = db_utils.list_of_Tickets()
    return jsonify(ticket_data(many=True).dump(ticket_data))


@api_blueprint.route("/ticketss/<int:ticket_id>", methods=["GET"])

def get_ticket_by_id(ticket_id):
    ticket = db_utils.get_entry_by_idd(Tickets, ticket_id)
    return jsonify(TicketData().dump(ticket))


@api_blueprint.route("/ticketss/<int:ticket_id>", methods=["DELETE"])

def delete_ticket(ticket_id):
    db_utils.delete_entry(Tickets, ticket_id)
    return jsonify(StatusResponse().dump({"code": 200}))
