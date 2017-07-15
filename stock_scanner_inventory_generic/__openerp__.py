# -*- coding: utf-8 -*-
# © 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Scanner Inventory Generic',
    'version': '8.0.1.0.0',
    'category': 'Inventory, Logistic, Storage',
    'license': 'AGPL-3',
    'summary': 'Generic stock_scanner scenario for inventory',
    'description': """
Stock Scanner Inventory Generic
===============================

This is a generic scenario for inventory with OCA's stock_scanner module.

This is inspired by Syleam's stock_scanner_inventory module, but it is quite different.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['stock_scanner'],
    'data': [
        #'data/account.xml',
        'data/Inventory.scenario',
    ],
    'installable': True,
}
