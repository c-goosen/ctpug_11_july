from openerp import fields, models, api
import logging
import datetime
from datetime import date
import time

_logger = logging.getLogger(__name__)

''' V8 api 

Module to add 'specials' to e-commerce.

Product on sale/special run as a campaign. Will tie into campaigns, products, etc.

'''


class product_specials_campaign(models.Model):
	_name     = "product.specials.campaign" 
	_description = "Campaing for Product Specials"

	name = fields.Char('Name')
	date_start = fields.Datetime('Start Date')
	date_end = fields.Datetime('End Date')
	category = fields.Char('Category')
	#product_specials = fields.One2many('product.specials', 'special_campaing_id')

	approved = fields.Boolean('Approved')

	special_price_reduction = fields.Float("Price reduction in for special")

	products = fields.One2many('product.product','product_campaign_special_id','Product')


	def change_product_price(self):
		ids =  context.get('active_id', False)

		campaign_rec = self.browse(ids)

		for product in campaign_rec.products:
			product.list_price = product.list_price * (campaign_rec.special_price_reduction/100)

	

product_specials_campaign()