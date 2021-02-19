# -*- coding: utf-8 -*-
# from odoo import http


# class PluginBiblio(http.Controller):
#     @http.route('/plugin_biblio/plugin_biblio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plugin_biblio/plugin_biblio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('plugin_biblio.listing', {
#             'root': '/plugin_biblio/plugin_biblio',
#             'objects': http.request.env['plugin_biblio.plugin_biblio'].search([]),
#         })

#     @http.route('/plugin_biblio/plugin_biblio/objects/<model("plugin_biblio.plugin_biblio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plugin_biblio.object', {
#             'object': obj
#         })
