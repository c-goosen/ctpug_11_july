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
    'name': 'uhwebo module',
    'version': '1.5',
    'author': 'Christo & Gutembert',
    'category': 'E-commerce',
    'sequence': 27,
    'summary': 'Module for Odoo implementation of ezohwebo',
    #'website': 'https://www.odoo.com/page/employees',
    'description': """
Ecommerce Module
=====================================


""",
    #'images': ['images/hr_allocation_requests.jpeg', 'images/hr_leave_requests.jpeg', 'images/leaves_analysis.jpeg'],
    'depends': ['hr', 'product', 'base'],
    'data': [

        #'hr_holidays_workflow.xml',
        #'hr_holidays_view.xml',
        
        ],
    #'demo': ['hr_holidays_demo.xml',],
    #'qweb': [
        'static/src/xml/*.xml',
    ],
    #'test': ['test/test_hr_holiday.yml',
    #        'test/hr_holidays_report.yml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
