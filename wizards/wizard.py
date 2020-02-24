# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'bookshelf.wizard'
    _description = "Wizard: Quick Registration of Authors to Books"

    def _default_author(self):
        return self.env['bookshelf.book'].browse(self._context.get('active_id'))

    author_id = fields.Many2one('bookshelf.author', string="Author", required=True,
                                default=_default_author, index=True)
    # book_ids = fields.One2many('bookshelf.book', 'author_id')

    name = fields.Char(required=True)
    nationality = fields.Char(default="Unknow")
    birthdate = fields.Date(required=True)

    @api.multi
    def subscribe(self):
        self.author_id.name = self.name
        self.author_id.nationality = self.nationality
        self.author_id.birthdate = self.birthdate

        return {}
