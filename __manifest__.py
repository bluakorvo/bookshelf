# -*_ coding: utf-8 -*-

{
    'name': "BookShelf",
    'summary': """Para registrar libros""",
    'author': "Jarsa Sistemas",
    'website': "R.RR",
    'category': "Uncategorized, Test, Postventa",
    'version': '12.0.0.0.1',

    'license': "GPL-3",

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/bookshelf.xml',
        'demo/demo_data.xml'
    ],
    'sequence': 1,
}
