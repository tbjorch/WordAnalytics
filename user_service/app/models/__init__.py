from user_service.app.models.User import User
from user_service.app.models.Role import Role
from user_service.app import db

user_roles = db.Table(
    db.Column(
        'user_id',
        db.Integer,
        db.ForeignKey('Users.id'),
        primary_key=True),
    db.Column(
        'role_id',
        db.Integer,
        db.ForeignKey('Roles.id'),
        primary_key=True)
)


db.create_all()
