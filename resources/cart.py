from flask_restful import Resource, reqparse, abort
from models import db, CartItem

class CartResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('image', type=str, required=True)
        parser.add_argument('price', type=float, required=True)
        args = parser.parse_args()

        cart_item = CartItem(**args)
        db.session.add(cart_item)
        db.session.commit()
        return {"message": "Cart item added successfully"}, 201

    def get(self, cart_id=None):
        if cart_id:
            cart_item = CartItem.query.get_or_404(cart_id)
            return {
                "id": cart_item.id,
                "name": cart_item.name,
                "image": cart_item.image,
                "price": cart_item.price
            }
        else:
            cart_items = CartItem.query.all()
            return [{
                "id": item.id,
                "name": item.name,
                "image": item.image,
                "price": item.price
            } for item in cart_items]

    def delete(self, cart_id):
        cart_item = CartItem.query.get_or_404(cart_id)
        db.session.delete(cart_item)
        db.session.commit()
        return {"message": "Cart item deleted successfully"}, 204
