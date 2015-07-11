# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'ctpug',
    'version' : '1.1',
    'sequence' : 2,
    'depends': ['hr', 'product', 'base'],
    'author' : 'Christo & Gutembert',
    'website' : 'www.odoo.zone',
    'email_1' : 'christo@christogoosen.co.za',
    'email_2' : 'gutembert@erpweb.co.za',
    'category':'ecommerce',
    'Description':"""
    Custom Module to enable the business rules 
    """,
    'demo' : [
            #'demo/partner.xml'
            #'demo/contract.xml',
            #'demo/contractor.xml',
            #'demo/salary.xml'
            ],
    #'test' : [''],
    'data' : [
            #'security/security_perm.csv',
            #'data/give_admin_tech_features.xml'
            'views/specials_campaign_view.xml',
            'views/menus.xml',

            ],
    'auto_install': False,
    'installable': True,
    'application': False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: