# -*- coding: utf-8 -*-
{
    'name': "Employee Dashboard Base",
    'summary': "Employee Dashboard",
    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and use
        JavaScript functionalities in Odoo 13.

        Source: https://www.youtube.com/playlist?list=PL-70MOdlCLUtjx80KMh5hh-MIGfWQMT4n
    """,
    'version': '13.0.1',
    'author': 'Ananthu Krishna',
    'website': 'http://www.codersfort.com/',
    'support': 'info@codersfort.com',
    'maintainer': 'Leonardo J. Caballero G. <leonardocaballero@gmail.com>',
    'license': 'AGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorial',
    # Any module necessary for this one to work correctly
    'depends': [
        'base',
        'web'
    ],
    # Always loaded
    'data': [
        'views/web_asset_backend_template.xml',
        'views/dashboard_view.xml'
    ],
    # Only loaded in demonstration mode
    'demo': [],
    # QWeb templates
    'qweb': [
        'static/src/xml/employee_dashboard.xml'
    ],
    'images': [
        'static/description/icon.png'
    ],
    'installable': True,
    'application': True,
}

