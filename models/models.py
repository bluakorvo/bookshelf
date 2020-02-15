# -*_ coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'bookshelf.book'
    _description = 'Books from BookShelf'

    name = fields.Char(string="Title", required=True)
    ISBN = fields.Char(string="ISBN", required=True)
    criticize = fields.Text()

    author_id = fields.Many2one('bookshelf.author', index=True)


class Author(models.Model):
    _name = 'bookshelf.author'
    _description = 'Autores en BookShelf'

    name = fields.Char(string="Nombre", required=True)
    nationality = fields.Char(default="Sin Cobijo")
    birthdate = fields.Date(default=fields.Date.today)

    book_ids = fields.One2many('bookshelf.book', 'author_id')