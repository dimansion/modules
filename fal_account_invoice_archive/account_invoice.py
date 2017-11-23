# -*- coding: utf-8 -*-

from osv import fields, orm
from tools.translate import _


class account_invoice(orm.Model):

    _inherit = "account.invoice"
    _columns = {
        'active': fields.boolean('Active', help="If the active field is set to False,\
         it will allow you to hide the payment term without removing it."),
    }

    _defaults = {
        'active': 1,
    }

    def action_archieve(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'active': False})

    def action_unarchieve(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'active': True})
