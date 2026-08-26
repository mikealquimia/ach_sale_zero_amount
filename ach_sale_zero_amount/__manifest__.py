# -*- coding: utf-8 -*-
{
    'name': "Approve Sale Order Zero Amount",
    'summary': """Module to approve sales with zero amount""",
    'description': """Module to approve sales with zero amount""",
    'author': "ACH Alchemical Code",
    'website': 'https://apps.odoo.com/apps/modules/browse?author=ACH%20Alchemical%20Code',
    'license': 'OPL-1',
    'support': 'mikealquimia@gmail.com',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'live_test_url': 'https://youtu.be/Qdi06kIFVMs',
    'price': 1.75,
    'currency': 'USD',
    'depends': ['base', 'sale'],
    'data': [
        'security/ach_sale_zero_amount_security.xml',
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
