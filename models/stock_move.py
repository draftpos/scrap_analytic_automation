# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    analytic_distribution = fields.Json(
        string='Analytic Distribution',
    )
    analytic_precision = fields.Integer(
        store=False,
        default=lambda self: self.env['decimal.precision'].precision_get('Percentage Analytic'),
    )

    def _generate_valuation_lines_data(self, partner_id, qty, debit_value, credit_value, debit_account_id, credit_account_id, description):
        res = super(StockMove, self)._generate_valuation_lines_data(partner_id, qty, debit_value, credit_value, debit_account_id, credit_account_id, description)
        
        distribution = self.analytic_distribution
        if not distribution and self.picking_id and self.picking_id.analytic_distribution:
            distribution = self.picking_id.analytic_distribution

        if distribution:
            valid_account_types = ['expense', 'expense_direct_cost', 'income', 'income_other']
            
            if res.get('debit_line_vals') and debit_account_id:
                debit_account = self.env['account.account'].browse(debit_account_id)
                if debit_account.account_type in valid_account_types:
                    res['debit_line_vals']['analytic_distribution'] = distribution
                    
            if res.get('credit_line_vals') and credit_account_id:
                credit_account = self.env['account.account'].browse(credit_account_id)
                if credit_account.account_type in valid_account_types:
                    res['credit_line_vals']['analytic_distribution'] = distribution
        return res

    def _get_account_move_line_vals(self):
        res = super(StockMove, self)._get_account_move_line_vals()
        
        distribution = self.analytic_distribution
        if not distribution and self.picking_id and self.picking_id.analytic_distribution:
            distribution = self.picking_id.analytic_distribution

        if distribution:
            valid_account_types = ['expense', 'expense_direct_cost', 'income', 'income_other']
            for line_vals in res:
                account_id = line_vals.get('account_id')
                if account_id:
                    account = self.env['account.account'].browse(account_id)
                    if account.account_type in valid_account_types:
                        line_vals['analytic_distribution'] = distribution
                
        return res
