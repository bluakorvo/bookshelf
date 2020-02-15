# -*_ coding: utf-8 -*-

{
    'name': "BookShelf",
    'summary': """Para registrar libros""",
    'description': """
    Para mantener actualizadas tus referencias
    """,
    'author': "A.M.G.B.",
    'website': "R.RR",
    'category': "Uncategorized",
    'version': '0.0.1-t',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/bookshelf.xml'
    ],
    'sequence': 1,
}