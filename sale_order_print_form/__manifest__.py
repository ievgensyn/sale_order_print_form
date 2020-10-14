{
    'name': 'Print SO form',

    'summary': 'Extending Sale functionality',

    'author': 'Ievgen Synchyshyn',
    'website': 'https://example.com/',

    'category': 'Sales',
    'license': 'Other proprietary',
    'version': '13.0.1.0.1',

    'depends': [
        'base', 'sale',
    ],
    'data': [
        'views/sale_order_view.xml',
        'report/order_report.xml.xml',
        'report/order_report_template.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
