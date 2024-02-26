from odoo import fields, models, api


class CancelTypeDismiss(models.Model):
    _name = "cancel.type.dismiss"
    
    name = fields.Char(string='')
    

class CancelTypeLost(models.Model):
    _name = "cancel.type.lost"
    
    name = fields.Char(string='')
    