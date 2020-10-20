import logging

from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    so_pf_amount_prepaid = fields.Monetary(
        string='Prepaid', compute='_compute_prepaid',
        default=0, )

    @api.depends('invoice_ids')
    def _compute_prepaid(self):
        for obj in self:
            obj.so_pf_amount_prepaid = 0
            paid_sum = \
                sum(obj.invoice_ids.mapped('amount_total')) - sum(
                    obj.invoice_ids.mapped('amount_residual'))
            obj.so_pf_amount_prepaid = paid_sum
