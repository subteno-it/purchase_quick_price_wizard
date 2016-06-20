 # -*- coding: utf-8 -*-
# Florent de Labarre - 2016

from openerp import api, fields, models, _


class PurchaseQuickPriceWizard(models.Model):
    _inherit = "purchase.order.line"
    _description = 'Purchase Quick Price Wizard'
    
    @api.multi
    def action_view_supplier_price(self, context=None):
        view_id = self.env.ref('purchase_quick_price_wizard.purchase_quick_price_wizard_view').id
        return {
            'name' : _('Product price : %s - %s' %(self.product_id.product_tmpl_id.default_code, self.product_id.product_tmpl_id.name)),
            'view_type':'form',
            'view_mode':'tree',
            'views' : [(view_id,'tree'),(False,'form')],
            'res_model':'product.supplierinfo',
            'view_id':view_id,
            'type':'ir.actions.act_window',
            'target':'new',
            'domain':"[('product_tmpl_id','=', %d)]" %self.product_id.product_tmpl_id.id
        }
       
       
class InvoiceQuickPriceWizard(models.Model):
    _inherit = "account.invoice.line"
    _description = 'Invoice Quick Price Wizard'
    
    @api.multi
    def action_view_supplier_price(self, context=None):
        view_id = self.env.ref('purchase_quick_price_wizard.purchase_quick_price_wizard_view').id
        return {
            'name' : _('Product price : %s - %s' %(self.product_id.product_tmpl_id.default_code, self.product_id.product_tmpl_id.name)),
            'view_type':'form',
            'view_mode':'tree',
            'views' : [(view_id,'tree'),(False,'form')],
            'res_model':'product.supplierinfo',
            'view_id':view_id,
            'type':'ir.actions.act_window',
            'target':'new',
            'domain':"[('product_tmpl_id','=', %d)]" %self.product_id.product_tmpl_id.id
        }
        
    