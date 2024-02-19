from odoo import api, fields, models


class HelpdeskImputationType(models.Model):
    _name = "helpdesk.time.imputation.type"
    
    name = fields.Char(string='')