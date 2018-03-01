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


{
    'name': 'Opencorp CMDB',
    'version': '1.0',
    'category': '',
    'sequence': 24,
    'description': """
    A configuration management database (CMDB) is a repository that acts as a data warehouse for information technology (IT) organizations. Its contents are intended to hold a collection of IT assets that are commonly referred to as configuration items (CI), as well as descriptive relationships between such assets. When populated, the repository becomes a means of understanding how critical assets such as information systems are composed, what their upstream sources or dependencies are, and what their downstream targets are.

La Configuration Management DataBase (abrégé CMDB), ou base de données de gestion de configuration, est une base de données unifiant les composants d'un système informatique. Elle permet de comprendre l'organisation entre ceux-ci et de modifier leur configuration. La CMDB est un composant fondamental d'une architecture ITIL.
    """,
    'author': 'OPENCORP',
    'website': 'http://www.opencorp.eu',
    'depends': [
        'project',
                ],
    'data': [
        'security/security.xml',
        'views/project_view.xml',
        'views/landscape_view.xml',
        'views/module_view.xml',
        'views/systeme_view.xml',
        'views/serveur_view.xml',
        'views/database_view.xml',
        'views/database_server_view.xml',
        'views/security/ir.model.access.csv',


    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
