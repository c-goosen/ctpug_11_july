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

	products = fields.One2many('product.product','product_campaign_special_id','Product')

	

product_specials_campaign()