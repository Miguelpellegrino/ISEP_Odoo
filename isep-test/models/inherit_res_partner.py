from odoo import models, fields, api
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    skill_ids = fields.Many2many('isep.skill', string="skill")