# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Ashram Visitor Registration',
    'version' : '0.1',
    'author' : 'Sree Hari Nagaralu',
    'sequence': 165,
    'category': 'Managing vehicles and contracts',
    'website' : 'https://www.odoo.com/page/maint',
    'summary' : 'Visitor Registration System',
    'description' : """
Registration System for Ashram Visitors
=======================================
Maintain visitor details for the ashram
""",
    'depends' : [
        'base',
    ],
    'data' : [
        'security/ir.model.access.csv',
		'visitors_view.xml',
		'visitors_data.xml',
    ],

    'demo': [],

    'installable' : True,
    'application' : True,
}
