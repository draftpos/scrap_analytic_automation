# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    analytic_distribution = fields.Json(
        string='Analytic Distribution',
        compute="_compute_analytic_distribution", store=True, readonly=False,
    )
    analytic_precision = fields.Integer(
        store=False,
        default=lambda self: self.env['decimal.precision'].precision_get('Percentage Analytic'),
    )

    @api.depends('move_ids', 'move_ids.analytic_distribution')
    def _compute_analytic_distribution(self):
        for picking in self:
            if not picking.analytic_distribution:
                picking.analytic_distribution = False

    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        if 'analytic_distribution' in vals:
            for picking in self:
                for move in picking.move_ids:
                    if not move.analytic_distribution:
                        move.analytic_distribution = picking.analytic_distribution
        return res
