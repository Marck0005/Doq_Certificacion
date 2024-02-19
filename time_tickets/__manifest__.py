# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Ticket management",
    "summary": "Model for the time tickets management",
    "version": "16.0.1.0.0",
    "category": "Sistema DOQ",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ['helpdesk_mgmt', 'hr_timesheet', 'analytic', 'account',],
    "data": [
        "security/ir.model.access.csv",
        "views/helpdesk_time_ticket.xml",
        "views/helpdesk_time_ticket_analytic_lines.xml",
        "wizards/wizard_team_report.xml",
        "views/helpdesk_time_ticket_team_view.xml",
        "views/reports.xml",
        "views/report_team_imputation.xml",
        "views/helpdesk_time_ticket_menus.xml",
        
        
        
        ],
}
