from odoo import models, fields, api
from odoo.exceptions import UserError
import random

class skill(models.Model):
    _name = 'isep.skill'
    
    @api.multi
    def write(self, vals):
        if not self._context.get('install_mode'):
            if self._skill_ref(self.id):
                raise UserError("you can't edit this skill")             
        return super(skill, self).write(vals)
    
    @api.multi
    def unlink(self):
        for record in self:
            self._skill_ref(record.id,("Deleting %s error, you not have permission to delete this skill" % (record.name)) ) 
        return super(skill, self).unlink() 

    name = fields.Char(string='name', comppute='_compute_complete_name')

    @api.constrains('name')
    def _generate_code(self):
        if self.search_count([('name', '=', self.name)]) > 1:
            raise UserError('This skill is already registered')

    def _skill_ref(self, id_write, message=None):
        for skill in [ self.env.ref('isep-test.skill_data_%s' % id) for id in range(1,7) ]:
            if id_write == skill.id:
                if message:
                    raise UserError(message)
                else:
                    return True
        return False