from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CustomerModel(db.Model):
    __tablename__ ="user"

    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
     #timestamp
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())


class ProductCategoryModel(db.Model):
    __tablename__ ="category"
    id= db.Column(db.Integer, primary_key=True)
    category_name=db.Column(db.String(25), nullable=False)

class Product(db.Model):
    __tablename__ ="product"
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25), nullable=False)
    description=db.Column(db.Text, nullable=False)
    image=db.Column(db.String(25), nullable=False)
    price=db.Column(db.Integer, nullable=False)

     # relationships
    category_id=db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)


class ShoppingCartModel(db.Model):
    __tablename__ ="cart"
    id= db.Column(db.Integer, primary_key=True)
    noProducts = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

class OrderModel(db.Model):
    __tablename__='orderdetails'
    id= db.Column(db.Integer, primary_key=True)    
    unit_price =db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    to_be_delivered_at=db.Column(db.TIMESTAMP, nullable=False)
    ordered_date=db.Column(db.TIMESTAMP, nullable=False)
    deliver_address =db.Column(db.String(25), nullable=False)
    payment_method =  db.Column(db.String(25), nullable=False)

    product_id=db.Column(db.Integer, db.ForeignKey("product.id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

class CartItem(db.Model):
    __tablename__='cartItems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    


