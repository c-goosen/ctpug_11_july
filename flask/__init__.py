from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import bootstrap
import xmlrpclib
from io import BytesIO
import base64

app = Flask(__name__)

import xmlrpclib

username = 'username' #the user
pwd = 'password'      #the password of the user
dbname = 'ctpug'    #the database

sock_common = xmlrpclib.ServerProxy ('http://127.0.0.1:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://127.0.0.1:8069/xmlrpc/object')


	
def test_connection(username,pwd,dbname):
	connection_reply = 'Connection to Odoo - '
	args = [] #query clause
	ids = sock.execute(dbname, uid, pwd, 'res.partner', 'search', args)

	fields = ['name', 'id', 'email'] #fields to read
	data = sock.execute(dbname, uid, pwd, 'res.partner', 'read', ids, fields)

	if data[0].name == 'admin':
		connection_reply + 'successful'
	else:
		connection_reply + 'not successful'
	return connection_reply

def get_products(username,pwd,dbname):
	args = [] #query clause
	ids = sock.execute(dbname, uid, pwd, 'product.product', 'search', args)

	fields = ['id', 'lst_price', 'qty_available', 'product_tmpl_id'] #fields to read
	data = sock.execute(dbname, uid, pwd, 'product.product', 'read', ids, fields)
	return data

def get_product_templates(username,pwd,dbname, args):
	args = args or [] #query clause
	ids = sock.execute(dbname, uid, pwd, 'product.template', 'search', args)

	fields = ['id', 'name', 'image_medium'] #fields to read
	data = sock.execute(dbname, uid, pwd, 'product.template', 'read', ids, fields)
	return data

def get_company_currency(username,pwd,dbname):
	args = []
	ids = sock.execute(dbname, uid, pwd, 'res.company', 'search', [('id','=',1)])

	fields = ['currency_id'] #fields to read
	company = sock.execute(dbname, uid, pwd, 'res.company', 'read', ids, fields)
	
	ids = sock.execute(dbname, uid, pwd, 'res.currency', 'search', [('id','=',company[0]['currency_id'][0])])
	fields = ['symbol']
	currency_symbol = sock.execute(dbname, uid, pwd, 'res.currency', 'read', ids, fields)
	return currency_symbol[0]['symbol']

@app.route('/products')
def products():
	product_output = 'List of products </br></br>'
	product_product = get_products(username,pwd,dbname)
	#product_template = get_product_templates(username,pwd,dbname)
	count = 0
	for x in product_product:
		args = [('id', '=', x['product_tmpl_id'][0])]
		product_template = get_product_templates(username,pwd,dbname,args)
		#product_output = product_output + product_template[0]['name']
		#product_output = ''+x['product_tmpl_id']
		#for y in product_template:
			#if x['product_tmpl_id'] == y['id']:
			#product_output = '\n |' + product_output + str(x['id']) + y['name'] + "<img style='display:block; width:100px;height:100px;' id='base64image' src='data:image/jpeg;base64, %s'/>" % y['image_medium'] +' | \n'
		if product_template[0]['image_medium']:
			product_output += '\n' + str(product_product[count]['id']) +' ' + product_template[0]['name'] + ' ' + get_company_currency(username,pwd,dbname) + str(product_product[count]['lst_price']) + "<img style='display:block; width:100px;height:100px;' id='base64image' src='data:image/jpeg;base64, %s'/>" % product_template[0]['image_medium'] +' \n'
		count += 1
	return  product_output
	#return 'List of products %s' % data[0]['id']

@app.route('/')
def index():
	connection_reply = 'Connection to Odoo - '
	args = [] #query clauses
	ids = sock.execute(dbname, uid, pwd, 'res.partner', 'search', args)

	fields = ['name', 'id', 'email'] #fields to read
	data = sock.execute(dbname, uid, pwd, 'res.partner', 'read', ids, fields)

	#return 'Hello %s' %data[0]

	if data[0]['id'] == 3:
		connection_reply =  '%s successful' % connection_reply
	else:
		connection_reply =  '%s not successful' % connection_reply
	return connection_reply
	#return render_template('index.html', title='Home', connection_reply=connection_reply)


if __name__ == '__main__':
    app.run(debug=True)
    Bootstrap(app)
    #return app
    #self.settings()
    #__main__.initiate_connection(username,pwd,dbname)
   #__main__.test_connection(username,pwd,dbname)

