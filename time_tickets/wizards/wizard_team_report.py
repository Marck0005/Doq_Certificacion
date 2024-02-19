from odoo import api, fields, models


class WizardTeamReport(models.TransientModel):
    _name = "wizard.team.report"
    _description = "Wizard for team report"
    
    initial_date = fields.Date(string='Initial date', required=True)
    final_date = fields.Date(string='Final date', required=True)
    client_id = fields.Many2one(comodel_name='res.partner', string='Client')
    team_id = fields.Many2one(comodel_name='helpdesk.time.ticket.team', string='Team')
    
    
    
    
    def report_team(self):
        data = {
        'model': self._name,
        'ids': self.ids,
        'form': self.read()[0],
        }
        return self.env.ref('time_tickets.team_imputation_report').report_action(self, data=data)