# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'CCPP',
    'version': '1',
    'category': 'customize',
    'sequence': 1001,
    'summary': 'CCPP',
    'description': "Project CCPP",
    'depends': ['base',
                'mail',
                'web',
                'project',
                'hr',
                'stock',
                'board',
                ],
    'data': [
        "data/ir_sequence.xml",
        "security/ir.model.access.csv",
        "views/project_view.xml",
        "views/ccpp_department_view.xml",
        "views/ccpp_priority_view.xml",
        "views/hr_department_view.xml",
        "views/ir_sequence_view.xml",
        "views/res_partner_view.xml",
        "views/ccpp_period_view.xml",
        "views/ccpp_customer_category_view.xml",
        "views/ccpp_province_view.xml",
        "views/ccpp_sale_target_view.xml",
        "views/ccpp_sale_target_period_view.xml",
        "views/ccpp_purchase_history_view.xml",
        "views/ccpp_dashboard_view.xml",
        "views/ccpp_customer_information_view.xml",
        "views/rocker_timesheet_views.xml",
        "views/ccpp_customer_budget_view.xml",
        "views/ccpp_approve_dashboard.xml",
        ],
    'qweb': [ 
        ],
    
    'installable': True,
    "application": True,
    'license': 'LGPL-3',
    'assets': {
    'web.assets_qweb': [
            #('remove','rocker_timesheet/static/src/xml/**/*'),
            #'ccpp/static/src/xml/**/*.xml',
            #'ccpp/static/src/xml/tree_button.xml',
    ],
    'web.assets_backend': [
            #'ccpp/static/src/sneat-bootstrap-html-admin-template/**/*',    
            'ccpp/static/src/js/**/*',
            'ccpp/static/src/scss/**/*',
            'ccpp/static/src/xml/**/*',
            'ccpp/static/src/views/*.xml',
            'ccpp/static/src/views/*.js',
            #('remove','rocker_timesheet/static/src/scss/rocker_calendar_button.scss'),
            #('remove','rocker_timesheet/static/src/js/rocker_calendar_button.js'),
            #('remove','rocker_timesheet/static/src/scss/rocker_roller_button.scss'),
            #('remove','rocker_timesheet/static/src/js/rocker_roller_button.js'),
            #('remove','rocker_timesheet/static/src/scss/rocker_tree_button.scss'),
            #('remove','rocker_timesheet/static/src/js/rocker_tree_button.js'),
        ],
    
    'web.assets_frontend':[        
    ],
    'web.assets_common' :[
    ]
    },
}