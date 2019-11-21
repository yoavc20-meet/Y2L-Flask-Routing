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
 	session.query(Product).all()
	session.commit()

def get_product(id):
	session.query(Product).filter_by(id=id)
	session.commit()

def Add_To_Cart(productID):
	product_Added = cart(
		productID=productID)
	session.add(product_Added)
	session.commit()


bb=add_product("the Uri", 29.99,"/theUri.jpeg","Ever dreamed of looking like Uri Etzion? this is the look for you!")
print(bb)