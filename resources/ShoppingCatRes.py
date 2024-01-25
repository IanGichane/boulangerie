from flask_restful import Resource, fields, reqparse, marshal_with, abort, request
from models import db, ShoppingCartModel
ShoppingCart_fields = {
    'id': fields.Integer,
    'noProducts': fields.Integer,
    'customer_id': fields.Integer,
}

class ShoppingCartResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('noProducts', help='Number of is required', required=True)
    parser.add_argument('customer_id', help='Customer id is required', required=True)

    
    @marshal_with(ShoppingCart_fields)
    def get(self, id=None):
        if id:
            cart= ShoppingCartModel.query.filter_by(id=id).first()
            if cart is not None:
                return cart
            else:
                abort(404, error=f"ShoppingCart {id=} not found")
        else:
            carts = ShoppingCartModel.query.all()
            return carts

    def post(self):
        data = ShoppingCartResource.parser.parse_args()
        cart = ShoppingCartModel(**data)

        try:
            db.session.add(cart)
            db.session.commit()
            return {"message":"created successfully"}, 200
        except:
            abort(500, error="Creation unsuccessful")

    def patch(self, id):
        data = request.json
        cart = ShoppingCartModel.query.filter_by(id=id).first()
        
        if not cart:
            abort(404, error="ShoppingCart not found")

        cart.noProducts = data.get('noProducts', cart.noProducts)  

        try:
            db.session.commit()
            return {"message": "updated successfully"}, 201
        except Exception as e:
            print(f"Error: {str(e)}")
            db.session.rollback()
            abort(500, error="Update unsuccessful")


    def delete(self, id):
        ShoppingCart = ShoppingCartModel.query.get(id)
        if ShoppingCart is None:
            abort(404, error="ShoppingCart not found")

        try:
            db.session.delete(ShoppingCart)
            db.session.commit()
            return {"message": f"ShoppingCart {id} deleted successfully"}
        except Exception as e:
            print(f"Error: {str(e)}")
            abort(500, error=f"Deletion for ShoppingCart {id} unsuccessful")
