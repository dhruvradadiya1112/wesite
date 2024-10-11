{
    'name': 'Website Product Discount',
    'version': '17.00.01',
    'summary': 'Apply discounts to products on the eCommerce website',
    'description': """
        This module allows you to set percentage-based discounts on products, 
        which are reflected on the eCommerce website's product listing and 
        product detail pages.
    """,
    'category': 'Website',
    'author': 'Dhruv Radadiya',
    'maintainer': 'Dhruv Radadiya',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'website_sale',
        'product',
        'base',
        'website',
        'sale_product_configurator',
    ],
    'data': [
        'views/product_template_views.xml',  # Backend view modification
        'views/cart_templates.xml',          # Cart and checkout templates (if modified)
        'views/website_product_template.xml', 
    ],
    'installable': True,
    
    'application': False,
    'auto_install': False,
}
