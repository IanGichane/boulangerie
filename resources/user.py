from flask_restful import Resource, reqparse, fields, marshal_with
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash
from models import CustomerModel, db

user_fields={
    "id":fields.Integer,
    "username":fields.String,
    "email":fields.String,
    "password":fields.String,
    "phone":fields.Integer
}

response_field = {
    "message": fields.String,
    "status": fields.String,
    "user": fields.Nested(user_fields)
}

class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help="username is required")
    # parser.add_argument('phone', required=True, help="Phone number is required")
    # parser.add_argument('email', required=True, help="Email address is required")
    # parser.add_argument('password', required=True, help="Password is required")

    @marshal_with(response_field)
    def post(self):
        data=Register.parser.parse_args()
        data['password']=generate_password_hash(data['password'])
        user=CustomerModel(**data)

        email=CustomerModel.query.filter_by(email=data['email']).one_or_none()
        if email:
            return "Email exists"

        try:
            db.session.add(user)
            db.session.commit()
            print(user)
            return {"message":"User created successfully"}      
        except:
            return {"message": "Unable to create account", "status": "fail"}

class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help="Email is required")
    parser.add_argument('password', required=True, help="Password is required")



    def post(self):
        data = Login.parser.parse_args()
        user = CustomerModel.query.filter_by(email=data['email']).first()

        if user:
            is_password_correct = check_password_hash(user.password, data['password'])
            if is_password_correct:
                access_token = create_access_token(identity=user.id)
                refresh_token = create_refresh_token(user.id)
                return {
                    "access_token": access_token,
                    "refresh_token": refresh_token
                },200
            return {"message":"User not authenticated"}
            
            
        return {"message": "Invalid email/password", "status": "fail"}

class refreshtokken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user)
        return {
            "access_token": new_token
        }