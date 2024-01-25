from flask_restful import Resource, fields, reqparse, marshal_with, abort, request
from models import db, OrderModel
order_fields = {
    'id': fields.Integer,
    'unit_price': fields.Integer,
    'quantity': fields.Integer,
    'to_be_delivered_at': fields.DateTime,
    'ordered_date': fields.DateTime,
    'deliver_address': fields.String,
    'payment_method': fields.String,
    'product_id': fields.Integer,
    'customer_id': fields.Integer,
}

class OrderResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('unit_price', help='Unit price is required', required=True)
    parser.add_argument('quantity', help='Quantity is required', required=True)
    parser.add_argument('to_be_delivered_at', help='Delivery time is required', required=True)
    parser.add_argument('ordered_date',  help='Ordered time is required', required=True)
    parser.add_argument('deliver_address', help='Address is required', required=True)
    parser.add_argument('payment_method', help='Pay method is required', required=True)
    parser.add_argument('product_id', help='Product is required', required=True)
    parser.add_argument('customer_id', help='Customer is required', required=True)
    
    @marshal_with(order_fields)
    def get(self, id=None):
        if id:
            order= OrderModel.query.filter_by(id=id).first()
            if order is not None:
                return order
            else:
                abort(404, error=f"Order {id} not found")
        else:
            orders = OrderModel.query.all()
            return orders

    def post(self):
        data = OrderResource.parser.parse_args()
        order = OrderModel(**data)

        try:
            db.session.add(order)
            db.session.commit()
            return {"message":"created successfully"}, 200
        except:
            abort(500, error="Creation unsuccessful")

    def patch(self, id):
        data = request.json
        order = OrderModel.query.filter_by(id=id).first()
        
        if not order:
            abort(404, error="order not found")

        order.quantity = data.get('quantity', order.quantity)  

        try:
            db.session.commit()
            return {"message": "updated successfully"}, 201
        except Exception as e:
            print(f"Error: {str(e)}")
            db.session.rollback()
            abort(500, error="Update unsuccessful")


    def delete(self, id):
        order = OrderModel.query.get(id)
        if order is None:
            abort(404, error="order not found")

        try:
            db.session.delete(order)
            db.session.commit()
            return {"message": f"order {id} deleted successfully"}
        except Exception as e:
            print(f"Error: {str(e)}")
            abort(500, error=f"Deletion for order {id} unsuccessful")
