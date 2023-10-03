# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('static', 'Por Aprobar')])
    zero_amount_approval = fields.Boolean(string="Aprobación monto cero")
    zero_amount_approval_user_id = fields.Many2one('res.users', string="Aprobador de Venta Monto Cero")

    @api.multi
    def action_confirm(self):
        for rec in self:
            if rec.amount_total == 0 and rec.zero_amount_approval == False:
                rec.write({'state':'static'})
                return
        res = super(SaleOrder, self).action_confirm()
        return res

    @api.multi
    def action_draft(self):
        for rec in self:
            if rec.amount_total == 0 and rec.zero_amount_approval == False:
                rec.write({'state':'draft'})
                return
        res = super(SaleOrder, self).action_draft()
        return res

    @api.multi
    def action_approve_zero_amount(self):
        self.write({'zero_amount_approval':True})
        self.write({'zero_amount_approval_user_id':self.env.user.id})
        self.action_confirm()