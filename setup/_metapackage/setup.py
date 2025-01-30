import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-akretion-stock-scanner-scenario",
    description="Meta package for akretion-stock-scanner-scenario Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-stock_scanner_inventory_generic',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 8.0',
    ]
)
