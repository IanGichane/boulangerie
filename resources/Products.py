from flask_restful import Resource, fields, reqparse, marshal_with, abort, request
from models import db, Product

product_fields={
    "id":fields.Integer,
    "name":fields.String,
    "description":fields.String,
    "image":fields.String,
    "price":fields.Integer,
    "category_id":fields.Integer
}

class ProductResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name is required', required=True)
    parser.add_argument('description', type=str, help='Description is required', required=True)
    parser.add_argument('image', type=str, help='Image is required', required=True)
    parser.add_argument('price', type=str, help='Price is required', required=True)
    parser.add_argument('category_id', type=str, help='product category is required', required=True)
    
    @marshal_with(product_fields)
    def get(self, id=None):
        if id:
            product = Product.query.filter_by(id=id).first()
            if product is not None:
                return product
            else:
                abort(404, error="Product not found")
        else:
            products = Product.query.all()
            return products

    def post(self):
        data = ProductResource.parser.parse_args()
        product = Product(**data)
        try:
            db.session.add(product)
            db.session.commit()
            return {"message":"created successfully"}, 200
        except:
            abort(500, error="Creation unsuccessful")

    def patch(self, id):
        data = request.json
        product = Product.query.filter_by(id=id).first()
        
        if not product:
            abort(404, error="productcategory not found")

        product.name = data.get('name', product.name) 
        product.price = data.get('price', product.price)  

        try:
            db.session.commit()
            return {"message": "updated successfully"}, 201
        except Exception as e:
            print(f"Error: {str(e)}")
            db.session.rollback()
            abort(500, error="Update unsuccessful")


    # def delete(self, id):
    #     productcategory = ProductCategoryModel.query.get(id)
    #     if productcategory is None:
    #         abort(404, error="Product not found")

    #     try:
    #         db.session.delete(productcategory)
    #         db.session.commit()
    #         return {"message": f"productcategory {id} deleted successfully"}
    #     except Exception as e:
    #         print(f"Error: {str(e)}")
    #         abort(500, error=f"Deletion for productcategory {id} unsuccessful")
