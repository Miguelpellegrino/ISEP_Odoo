from odoo import api, fields, models
from odoo.exceptions import UserError

class isep_report(models.TransientModel):
    _name = 'isep.report.wizard'
    _description = 'report'

    developer_id = fields.Many2one('isep.developer', string="developer")

    def print_pdf(self):
        if not self.developer_id:
            raise UserError('must choose a developer')

        developer = self.env['isep.developer'].search([(
            'id','=', self.developer_id.id
        )])

        content_pdf = {
            'developer':developer.id,
            'partner_id':developer.partner_id.name,
            'skills': [skill.name for skill in developer.skill_id],
            'name':developer.name,
            'years':developer.years,
            'percent':developer.percent,
            'age':developer.age,
            'student':developer.student,
            'company_id_name':developer.company_id.name
        }

        return self.env.ref('isep-test.report_developer').report_action(self,data=content_pdf)