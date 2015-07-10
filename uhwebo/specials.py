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


class product_specials(models.Model):
	_name     = "product.specials" 
	_description = "Product Specials"

product_specials()