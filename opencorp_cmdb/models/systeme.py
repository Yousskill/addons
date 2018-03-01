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


class systeme(models.Model):
    _name = "systeme"
    name = fields.Char(u'Instance', size=128)
    landscape_id = fields.Many2one('project.landscape', 'Landscape')
    ip = fields.Char('URL', size=128)
    #'mac':fields.char('MAC',size=128),
    serveur_id = fields.Many2one('serveur', 'Serveur', size=128)
    user = fields.Char('User admin', size=128)
    password = fields.Char('Password', size=128)
    database_ids = fields.One2many('database', 'instance_id', 'Database')

    def get_user(self, cr, uid, ids, context=None):
        systems = self.search(cr, uid, [])
        for s in self.browse(cr, uid, systems, context):
            self.write(cr, uid, [s.id], {'user': s.serveur_id.user, 'password': s.serveur_id.password})
        return True


class serveur(models.Model):
    _name = "serveur"
    name = fields.Char('Name', size=128)
    ip = fields.Char('IP', size=128)
    mac = fields.Char('MAC', size=128)
    user = fields.Char('User admin', size=128)
    password = fields.Char('Password', size=128)
