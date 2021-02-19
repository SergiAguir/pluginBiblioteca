# -*- coding: utf-8 -*-

from odoo import models, fields, api


class biblio(models.Model):
    _name = 'biblioteca.persona_model'
    _inherit = 'biblioteca.persona_model'
    
    provincia = fields.Char(string="Provincia")