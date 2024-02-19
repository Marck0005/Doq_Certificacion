from odoo import api, fields, models


class HelpdeskAnalyticLines(models.Model):
    _name = "helpdesk.time.analytic.lines"
    inherit = ['account.analytic.line', 'hr.employee']
    
    ticket_id = fields.Many2one(comodel_name='helpdesk.time.ticket', string='')
    team_id = fields.Many2one(comodel_name='helpdesk.time.ticket.team', string='Team', related='ticket_id.team_id')
    
    imputation_date = fields.Date(string='', default=fields.Date.context_today)
    unit_amount = fields.Float(string='')
    imputation_type_id = fields.Many2one(comodel_name='helpdesk.time.imputation.type', string='')
    employee_id = fields.Many2one(comodel_name='hr.employee', string='', default = lambda self: self.env.user.employee_id)
    company_id = fields.Many2one(comodel_name='res.company', string='', default = lambda self: self.env.company)
    account_id = fields.Many2one(comodel_name='account.analytic.account', string='')#Proyecto asociado
    description = fields.Char(string='')
    
    timesheet_cost = fields.Float(string='', compute='_compute_timesheet_cost')
    
    @api.depends('unit_amount', 'employee_id.hourly_cost')
    def _compute_timesheet_cost(self):
        #Con el empleado en cuestion calcular el coste de lo que ha hecho(unit_amount)*coste de la hora(hourly_cost)
        for record in self:
            record.timesheet_cost = record.unit_amount * record.employee_id.hourly_cost
    
    
    