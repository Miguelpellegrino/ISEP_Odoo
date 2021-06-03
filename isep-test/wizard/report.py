from odoo import api, fields, models
from odoo.exceptions import UserError

class isep_report(models.TransientModel):
    _name = 'isep.report.wizard'
    _description = 'report'

    developer = fields.Many2one('isep.developer', string="developer")

    def print_pdf(self):
        developer = self.env['isep.developer'].search([(
            'id','=', self.developer.id
        )])
        content_pdf = {
            'developer':developer.id,
            'partner_id':developer.partner_id.name
        }

        return self.env.ref('isep-test.report_developer').report_action(self,data=content_pdf)