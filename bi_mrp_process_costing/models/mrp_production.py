from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    estimated_material_cost = fields.Float(string="Estimated Material Cost")
    estimated_labor_cost = fields.Float(string="Estimated Labor Cost")
    estimated_overhead_cost = fields.Float(string="Estimated Overhead Cost")
    estimated_total_cost = fields.Float(string="Estimated Total Cost", compute="_compute_estimated_total", store=True)

    actual_material_cost = fields.Float(string="Actual Material Cost", compute="_compute_actual_costs", store=True)
    actual_labor_cost = fields.Float(string="Actual Labor Cost", compute="_compute_actual_costs", store=True)
    actual_overhead_cost = fields.Float(string="Actual Overhead Cost", compute="_compute_actual_costs", store=True)
    actual_total_cost = fields.Float(string="Actual Total Cost", compute="_compute_actual_costs", store=True)

    cost_difference = fields.Float(string="Cost Difference", compute="_compute_actual_costs", store=True)

    @api.depends('move_raw_ids', 'workorder_ids.duration_expected', 'workorder_ids.workcenter_id')
    def _compute_actual_costs(self):
        for rec in self:
            material_cost = sum(
                line.product_id.standard_price * line.quantity
                for move in rec.move_raw_ids
                for line in move.move_line_ids
            )

            labor_cost = sum([
                (wo.duration_expected or 0) / 60.0 * (wo.workcenter_id.labor_cost_per_hour or 0)
                for wo in rec.workorder_ids
            ])

            overhead_cost = sum([
                (wo.duration_expected or 0) / 60.0 * (wo.workcenter_id.overhead_cost_per_hour or 0)
                for wo in rec.workorder_ids
            ])

            rec.actual_material_cost = material_cost
            rec.actual_labor_cost = labor_cost
            rec.actual_overhead_cost = overhead_cost
            rec.actual_total_cost = material_cost + labor_cost + overhead_cost

            rec.cost_difference = rec.estimated_total_cost - rec.actual_total_cost

    @api.depends('estimated_material_cost', 'estimated_labor_cost', 'estimated_overhead_cost')
    def _compute_estimated_total(self):
        for rec in self:
            rec.estimated_total_cost = (
                    rec.estimated_material_cost +
                    rec.estimated_labor_cost +
                    rec.estimated_overhead_cost
            )
