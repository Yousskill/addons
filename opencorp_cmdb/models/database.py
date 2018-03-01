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


class database_server(models.Model):
    _name = "database.server"
    name = fields.Char(u'Name', size=128)
    version = fields.Char('Version', size=128)


class database(models.Model):
    _name = "database"
    name = fields.Char(u'Name', size=128),
    user = fields.Char('User admin', size=128)
    password = fields.Char('Password', size=128)
    db_server_id = fields.Many2one('database.server', 'Database server')
    instance_id = fields.Many2one('systeme', 'Instance')


