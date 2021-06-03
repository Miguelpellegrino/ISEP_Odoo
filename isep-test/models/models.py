# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
class developer(models.Model):
    _name = 'isep.developer'

    @api.multi
    def unlink(self):
        for record in self:
            res_partner = self.env['res.partner'].search([('id', '=', record.partner_id.id)])
            if record.skill_id:
                res_partner.write({
                    'skill_ids':[(6, 0, [])]
                })
        return super(developer, self).unlink()

    @api.onchange('partner_id','skill_id','percent')
    def _compute_complete_name(self):
        for content in self:
            if content.partner_id and content.skill_id and content.percent:
                self.name = '%s/ %s/ %s' % (content.partner_id.name, [skill.name for skill in content.skill_id], content.percent)

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    name = fields.Char(string='name', computed='_compute_complete_name', readonly=True, store=True)
    skill_id = fields.Many2many('isep.skill', string='skill')
    years = fields.Integer(string='Year',required=True, default=1)
    percent = fields.Float(string='percent',required=True)
    company_id = fields.Many2one('res.company', string='company',required=True)
    age = fields.Integer(string="age", required=True)
    student = fields.Boolean(string="student", default=False)

    @api.constrains('percent','partner_id')
    def _generate_code(self):
        if self.percent > 100:
            raise UserError('Your knowledge percentage cannot exceed 100%')
        if self.search_count([('partner_id','=', self.partner_id.id)]) > 1:
            raise UserError('There is already a record for this partner')

    @api.constrains('skill_id')
    def write_res_partner(self):
        res_partner = self.env['res.partner'].search([('id', '=', self.partner_id.id)])
        if self.skill_id:
            res_partner.write({
                'skill_ids':[(6, 0, self.skill_id.ids)]
            })