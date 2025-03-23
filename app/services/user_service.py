from app.models.user import User
from app.models.base import db
from app.schemas.user import user_schema, users_schema

class UserService:
    @staticmethod
    def get_all_users():
        users = User.query.all()
        return users_schema.dump(users)

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)

    @staticmethod
    def create_user(data):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get_or_404(user_id)
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return user_schema.dump(user)

    @staticmethod
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return True 