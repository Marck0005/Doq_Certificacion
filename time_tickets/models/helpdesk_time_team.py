from odoo import api, fields, models


class HelpdeskTeam(models.Model):
    _name = 'helpdesk.time.ticket.team'
    _inherit = ['helpdesk.ticket.team']
    
        
    user_ids = fields.Many2many(
        'res.users', 
        'helpdesk_time_ticket_team_user_rel', 
        'team_id', 
        'user_id', 
        string='Members',
    )
    
    ticket_ids = fields.One2many(
         comodel_name="helpdesk.time.ticket",
         inverse_name="team_id",
         string="Tickets",
    )
    
    time_report = fields.Boolean(string='')
    
    team_total_time = fields.Float(string='', compute='_compute_team_total_time', store=True)
    
    @api.depends('ticket_ids.total_time')
    def _compute_team_total_time(self):
        for record in self:
            record.team_total_time = sum(record.ticket_ids.mapped('total_time'))
            
            
    def launch_wizard_team_report(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Team Report',
            'res_model': 'wizard.team.report',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_team_id': self.id,
            }
        }