from flask_restful import Resource, fields, reqparse, marshal_with, abort, request
from models import db, ProductCategoryModel

productcategory_fields = {
    'id': fields.Integer,
    'category_name': fields.String,
    
}

class ProductCategoryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('category_name', type=str, help='productcategory is required', required=True)
    
    @marshal_with(productcategory_fields)
    def get(self, id=None):
        if id:
            category = ProductCategoryModel.query.filter_by(id=id).first()
            if category is not None:
                return category
            else:
                abort(404, error="Productcategory not found")
        else:
            categories = ProductCategoryModel.query.all()
            return categories

    def post(self):
        data = ProductCategoryResource.parser.parse_args()
        productcategory = ProductCategoryModel(**data)
        try:
            db.session.add(productcategory)
            db.session.commit()
            return {"message":"created successfully"}, 200
        except:
            abort(500, error="Creation unsuccessful")

    def patch(self, id):
        data = request.json
        productcategory = ProductCategoryModel.query.filter_by(id=id).first()
        
        if not productcategory:
            abort(404, error="productcategory not found")

        productcategory.category_name = data.get('category_name', productcategory.category_name)  

        try:
            db.session.commit()
            return {"message": "updated successfully"}, 201
        except Exception as e:
            print(f"Error: {str(e)}")
            db.session.rollback()
            abort(500, error="Update unsuccessful")


    def delete(self, id):
        productcategory = ProductCategoryModel.query.get(id)
        if productcategory is None:
            abort(404, error="Product not found")

        try:
            db.session.delete(productcategory)
            db.session.commit()
            return {"message": f"productcategory {id} deleted successfully"}
        except Exception as e:
            print(f"Error: {str(e)}")
            abort(500, error=f"Deletion for productcategory {id} unsuccessful")
