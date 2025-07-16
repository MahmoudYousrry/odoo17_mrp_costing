from odoo import models, fields

class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    labor_cost_per_hour = fields.Float(string="Labor Cost per Hour", help="Hourly cost of labor for this work center.")
    overhead_cost_per_hour = fields.Float(string="Overhead Cost per Hour", help="Hourly overhead cost for this work center.")
