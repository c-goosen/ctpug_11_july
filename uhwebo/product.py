from openerp import fields, models, api
import logging
import datetime
from datetime import date
import time

_logger = logging.getLogger(__name__)

''' V8 api 
Inherit and add field to product product

'''


class product_product(models.Model):
	_inherit = 'product.product'

	product_campaign_special_id = fields.Many2one('product.specials.campaign')
	special 					= fields.Boolean('Special') 
	ecommerce_product			= fields.Boolean('Sell on website')
	

product_product()

class product_template(models.Model):
	_inherit = 'product.template'

	special 	= fields.Boolean('Special') 

product_template()
