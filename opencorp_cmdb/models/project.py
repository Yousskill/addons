# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from odoo import api, fields, models


class project_project(models.Model):
    _inherit = "project.project"
    module_ids = fields.Many2many('project.module', 'module_id', 'project_id', string='Modules')
    landscape_id = fields.Many2one('project.landscape', 'Landscape')


class project_task(models.Model):
    _inherit = "project.task"
    module_id = fields.Many2one('project.module', 'Module')
    printscreen_ids = fields.One2many('printscreen', 'task_id', 'Printscreens')


class printscreen(models.Model):
    _name="printscreen"
    name = fields.Char('Name', size=1028)
    attach = fields.Binary('Attachment')
    task_id = fields.Many2one('project.task', 'Task')


