from marshmallow import validate, Schema, fields
from flask_bcrypt import generate_password_hash


class Credentials(Schema):
    email = fields.String(validate=validate.Email())
    password = fields.String()


class ListUsersRequest(Schema):
    idd = fields.Integer()
    email = fields.String(validate=validate.Email())
    first_name = fields.String()
    last_name = fields.String()


class UserData(Schema):
    idd = fields.Integer()
    name = fields.String()
    email = fields.String(validate=validate.Email())
    password = fields.String()
    first_name = fields.String()
    last_name = fields.String()


class UserToCreate(Schema):
    idd = fields.Integer()
    name = fields.String()
    email = fields.String(validate=validate.Email())
    password = fields.Function(
        deserialize=lambda obj: generate_password_hash(obj), load_only=True
    )
    first_name = fields.String()
    last_name = fields.String()


class UserToUpdate(Schema):
    idd = fields.Integer()
    name = fields.String()
    email = fields.String(validate=validate.Email())
    password = fields.Function(
        deserialize=lambda obj: generate_password_hash(obj), load_only=True
    )
    first_name = fields.String()
    last_name = fields.String()

class TicketData(Schema):
    ticketid = fields.Integer()
    name = fields.String()
    price = fields.Integer()
    status = fields.Integer()
    owner_id = fields.Integer()


class TicketToCreate(Schema):
    ticketid = fields.Integer()
    name = fields.String()
    price = fields.Integer()
    status = fields.Integer()
    owner_id = fields.Integer()

class StatusResponse(Schema):
    code = fields.Integer()
    type = fields.String(default="OK")
    message = fields.String(default="OK")
