# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    analytic_distribution = fields.Json(
        string='Analytic Distribution',
        compute="_compute_analytic_distribution",
        store=True,
    )
    analytic_precision = fields.Integer(
        store=False,
        default=lambda self: self.env['decimal.precision'].precision_get('Percentage Analytic'),
    )

    @api.depends('line_ids.analytic_distribution')
    def _compute_analytic_distribution(self):
        for move in self:
            # Try to find the first line with an analytic distribution and use it for the header display
            distribution = False
            for line in move.line_ids:
                if line.analytic_distribution:
                    distribution = line.analytic_distribution
                    break
            move.analytic_distribution = distribution
