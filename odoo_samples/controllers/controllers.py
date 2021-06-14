# -*- coding: utf-8 -*-
# from odoo import http


# class OdooSamples(http.Controller):
#     @http.route('/odoo_samples/odoo_samples/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_samples/odoo_samples/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_samples.listing', {
#             'root': '/odoo_samples/odoo_samples',
#             'objects': http.request.env['odoo_samples.odoo_samples'].search([]),
#         })

#     @http.route('/odoo_samples/odoo_samples/objects/<model("odoo_samples.odoo_samples"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_samples.object', {
#             'object': obj
#         })
