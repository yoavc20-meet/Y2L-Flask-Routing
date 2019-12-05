from model import Base, Product, cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_product(name, price,picture_link, description):
	product_object = Product(
		name=name,
		price=price,
		picture_link=picture_link,
		description=description)
	session.add(product_object)
	session.commit()

def edit_product(id):
	Product = session.query(Product).filter_by(id=id)
	Product.name=name
	Product.price=price
	Product.picture_link=picture_link
	Product.description=description
	session.commit()

def delete_product(id):
	session.query(Product).filter_by(
	id=id).delete()
	session.commit()

def all_products():
 	return session.query(Product).all()
	

def get_product(id):
	session.query(Product).filter_by(id=id)
	session.commit()

def Add_To_Cart(productID):
	product_Added = cart(
		productID=productID)
	session.add(product_Added)
	session.commit()

def all_added():
	return session.query(cart).all()

def delete_cart(productID):
	session.query(cart).filter_by(
	productID=productID).delete()
	session.commit()


# delete_cart(1)
# Add_To_Cart(1)
# add_product("The Uri", 24.99, "static/theUri.jpeg", "Ever dreamed of looking like Uri Etzion? this is the look for you!")
# add_product("The Clean Look(Toby's favourite!)", 29.99, "static/clean.jpg", "You don't like facial hair? this is the look for you!")
# add_product("The James Harden)",34.99, "static/harden.jpeg", "Ever dreamed of having a huge beard and making all your friends jealous? this is the look for you!")
# delete_product()
# delete_product(9)
# delete_product(8)