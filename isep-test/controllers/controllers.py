# -*- coding: utf-8 -*-
from odoo import http

# class Isep-test(http.Controller):
#     @http.route('/isep-test/isep-test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/isep-test/isep-test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('isep-test.listing', {
#             'root': '/isep-test/isep-test',
#             'objects': http.request.env['isep-test.isep-test'].search([]),
#         })

#     @http.route('/isep-test/isep-test/objects/<model("isep-test.isep-test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('isep-test.object', {
#             'object': obj
#         })