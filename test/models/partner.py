# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _name = 'openacademy.partner'
    _inherits = {
        'res.partner': 'res_partner_id'
    }
    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)

    res_partner_id = fields.Many2one('res.partner', string="related partner")