# -*_ coding: utf-8 -*-
from odoo import models, exceptions, fields, api


class Book(models.Model):
    _name = 'bookshelf.book'
    _description = 'Books from BookShelf'

    name = fields.Char(string="Title", required=True)
    criticize = fields.Text()
    isbn = fields.Char(required=True)

    author_id = fields.Many2one('bookshelf.author', index=True)

    _sql_constraints = [
        ('ISBN_unique',
         'UNIQUE(isbn)',
         "ERROR: El ISBN debe ser unico"),
    ]


class Author(models.Model):
    _name = 'bookshelf.author'
    _description = 'Autores en BookShelf'

    name = fields.Char(string="Nombre", required=True)
    nationality = fields.Char(default="Unknow")
    birthdate = fields.Date(required=True)

    book_ids = fields.One2many('bookshelf.book', 'author_id')
