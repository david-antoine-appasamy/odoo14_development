# -*- coding: utf-8 -*-
{
    'name': "Student Record",

    'summary': """
       This module will add a record to store student details""",

    'description': """
        This module will add a record to store student details
    """,

    'author': "My Company",
    'website': "http://www.yoganandam.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Testing Tools',
    'version': '10.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
