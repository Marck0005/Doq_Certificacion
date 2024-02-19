from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _name = "helpdesk.time.ticket"
    _inherit = ['helpdesk.ticket']
    
    team_id = fields.Many2one(
        comodel_name="helpdesk.time.ticket.team",
        string="Team",
        index=True,
    )
    
    time_report = fields.Boolean(related='team_id.time_report', string='Time Report')
    
    total_time = fields.Float(string='', compute='_compute_total_time', store=True)
    time_analytic_lines_ids = fields.One2many(comodel_name='helpdesk.time.analytic.lines', inverse_name='ticket_id', string='')  
    
    @api.depends('time_analytic_lines_ids.unit_amount')
    def _compute_total_time(self):
        for record in self:
            record.total_time = sum(record.time_analytic_lines_ids.mapped('unit_amount'))
  
    