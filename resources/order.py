from flask_restful import Resource, fields, marshal_with, reqparse

from models import OrderModel, db


class Orders(Resource):
    def post(self):
        def get(self, id=None):
            if id:
                orders = OrderModel.query.filter_by(id=id).first()
                return property
            else:
                orders = OrderModel.query.all()

            return properties

      
