# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    analytic_distribution = fields.Json(
        string='Analytic Distribution',
    )
    analytic_precision = fields.Integer(
        store=False,
        default=lambda self: self.env['decimal.precision'].precision_get('Percentage Analytic'),
    )

    def _prepare_move_values(self):
        res = super(StockScrap, self)._prepare_move_values()
        if self.analytic_distribution:
            res['analytic_distribution'] = self.analytic_distribution
        return res
