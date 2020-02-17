# -*_ coding: utf-8 -*-

{
    'name': "BookShelf",
    'summary': """Para registrar libros""",
    'description': """
    Para mantener actualizadas tus referencias
    """,
    'author': "A.M.G.B.",
    'website': "R.RR",
    'category': "Uncategorized, Test, Postventa",
    'version': '12.0.0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/bookshelf.xml',
        'demo/demo_data.xml'
    ],
    'sequence': 1,
}
