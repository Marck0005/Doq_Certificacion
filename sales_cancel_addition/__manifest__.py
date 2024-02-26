# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sales cancel addition",
    "summary": "Sistema DOQ Curso Sistema DOQ",
    "version": "16.0.1.0.0",
    "category": "Sistema DOQ",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ["sale" , "base"],
    "data": [
        "security/ir.model.access.csv",
        "wizards/wizard_cancel_sale.xml",
        "views/sale_order.xml",
        ],
}
