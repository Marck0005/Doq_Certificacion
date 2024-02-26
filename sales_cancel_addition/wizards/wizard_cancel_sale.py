from odoo import api, fields, models


class WizardCancelSale(models.TransientModel):
    _name = "wizard.cancel.sale"
    
    
    cancel_type = fields.Selection(
        string='',
        selection=[('dismissed', 'Dismissed'), ('lost', 'Lost'), ('won', 'Won')],
        required = True,
    )
    
    cancel_type_dismiss_id = fields.Many2one(string = '', comodel_name = 'cancel.type.dismiss')
    cancel_type_lost_id = fields.Many2one(string = '', comodel_name = 'cancel.type.lost' )
    
    cancel_description = fields.Char(
        string='',
        required = True,
    )
    
    def cancel_sale(self):
        self.ensure_one()
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
        sale_order.cancel_type = self.cancel_type
        sale_order.cancel_description = self.cancel_description
        
        if sale_order.cancel_type == 'won':
            sale_order.action_confirm()
        else:
            sale_order.action_cancel()
            
        return {'type': 'ir.actions.act_window_close'}
    