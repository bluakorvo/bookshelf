# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'bookshelf.wizard'
    _description = "Wizard: Quick Registration of Authors to Books"

    def _default_author(self):
        return self.env['bookshelf.book'].browse(self._context.get('active_id'))

    author_id = fields.Many2one('bookshelf.author', string="Author", required=True,
                                default=_default_author, index=True)

    def _default_author_name(self):
        return self.author_id.name

    def _default_author_country(self):
        return self.author_id.nationality

    def _default_author_birthdate(self):
        return self.author_id.birthdate

    name = fields.Char(required=True, default=_default_author_name)
    nationality = fields.Char(default=_default_author_country)
    birthdate = fields.Date(default=_default_author_birthdate)

    @api.multi
    def modify_author(self):
        self.author_id.name = self.name
        self.author_id.nationality = self.nationality
        self.author_id.birthdate = self.birthdate

        return {}
