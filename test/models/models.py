# -*- coding: utf-8 -*-

from odoo import models, fields, api
class test(models.Model):
    _inherit = 'purchase.order'
    
    @api.multi
    def activity_update(self):
        self.env['mail.activity.mixin'].activity_schedule('hr_expense.mail_act_expense_approval',user_id=self.env.user.id)