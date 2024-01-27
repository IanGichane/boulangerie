from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import  Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db
from resources.user import Register,Login,refreshtokken
from resources.productcategoryres import ProductCategoryResource
from resources.order import OrderResource
from resources.Products import ProductResource
from resources.ShoppingCartRes import ShoppingCartResource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret" 
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(refreshtokken, '/refresh')
api.add_resource(ProductResource, '/products', "/products/<int:id>")
api.add_resource(ProductCategoryResource, '/categories', "/categories/<int:id>")
api.add_resource(OrderResource, '/orders', "/orders/<int:id>")
api.add_resource(ShoppingCartResource, '/carts', '/carts/<int:id>')

if __name__ == '__main__':
    app.run(port=5556)
