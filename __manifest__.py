# -*- coding: utf-8 -*-
{
    'name': "Scrap & Transfer Analytic Automation",
    'summary': """
        Automatically apply analytic distributions from Internal Transfers and Scraps to resulting journal entries.
    """,
    'description': """
        This module allows you to set an Analytic Distribution at the header level of Internal Transfers and Scrap Orders,
        as well as at the line level (Operations). 
        The distribution set on the line will override the header level.
        Upon validation, the analytic distribution is seamlessly passed to the generated Journal Entry (Inventory Valuation).
    """,
    'author': "Your Company",
    'website': "https://www.yourcompany.com",
    'category': 'Inventory/Inventory',
    'version': '1.0',
    'depends': ['base', 'stock', 'account', 'stock_account', 'analytic'],
    'data': [
        'views/stock_picking_views.xml',
        'views/stock_scrap_views.xml',
        'views/stock_picking_tree_views.xml',
        'views/stock_scrap_tree_views.xml',
        'views/account_move_tree_views.xml',
    ],
    'license': 'LGPL-3',
}
