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


@app.route('/cart', methods=['GET', 'POST'] )
def cart():
	if request.method == 'POST':	
		added= request.form['added']
		Add_To_Cart(added)
		return render_template("cart.html", carts= all_added())
	else:
		return render_template("cart.html",carts=all_added())



if __name__ == '__main__':
    app.run(debug=True)