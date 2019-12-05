from flask import Flask, request, redirect, url_for, render_template,request
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
app.secret_key = "MY_SUPER_SECRET_KEY"



##### Code here ######
@app.route('/')
def home():
	return render_template("home.html")


@app.route('/store')
def store():
	return render_template("store.html",products=all_products())

@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/cart/<int:productID>')
def cart(productID):
	return render_template("cart.html",carts=all_added(),productID=productID)

##################### the problem happened when i tried doing the using 
#of the integer in app route cart
#


if __name__ == '__main__':
    app.run(debug=True)