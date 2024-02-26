from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    cancel_type = fields.Selection(
        string='',
        selection=[('active', 'Active'),('dismissed', 'Dismissed'), 
                   ('lost', 'Lost'), ('won', 'Won')],
        default = 'active',
    )
    
    cancel_description = fields.Char(string='')
    
    
    def launch_cancel_sale_wizard(self):
        if self.cancel_type == 'won' or self.state == 'sale':
            self.action_draft()
            
        else:
            return {
                'name': 'Cancel Sale Order',
                'type': 'ir.actions.act_window',
                'res_model': 'wizard.cancel.sale',
                'view_mode': 'form',
                'view_id': self.env.ref('sales_cancel_addition.wizard_cancel_sale_view_form').id,
                'target': 'new',
                'context': {'default_sale_order_id': self.id}
            }
        
    def action_draft(self):
        self.cancel_type = 'active'
        self.state = 'cancel'
        return super(SaleOrder, self).action_draft()
    
    def action_confirm(self):
        self.cancel_type = 'won'
        return super(SaleOrder, self).action_confirm()
    
    def set_cancel_type(self):
        for rec in self:
            if rec.state == 'sale':
                rec.cancel_type = 'won'
    
    
  
        