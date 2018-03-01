# -*- coding: utf-8 -*-

import random
from odoo import models, fields, api


class ComputedModel(models.Model):
    _name = 'openacademy.computed'

    name = fields.Char(compute='_compute_name')
    description = fields.Text(compute='_compute_desc')
    value = fields.Integer()

    @api.multi
    def _compute_name(self):
        try:
            print(self.ensure_one(), "multi")
        except ValueError:
            print("désolé")
        else:
            for record in self:
                record.name = str(random.randint(1, 1e6))
    # @api.one
    # def _compute_name(self):
    #     for record in self:
    #         record.name = str(random.randint(1, 1e6))
    #     print(self, "one")

    @api.depends('value')
    def _compute_desc(self):
        for record in self:
            record.description = "Record with value %s" % record.value