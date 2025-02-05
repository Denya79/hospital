import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class HHDoctor(models.Model):

    _name = 'hr.hospital.doctor'
    _inherit = 'hr_hospital_person'
    _description = 'Doctor'

    name = fields.Char()
    description = fields.Text()

    active = fields.Boolean(
        default=True
    )
    specialty = fields.Selection([
        ('pharmacist','Pharmacist'),
        ('family_doctor','Family doctor'),
        ('neurologist','Neurologist'),
    ], string='Speciality')

    is_intern = fields.Boolean(string='Intern')
    mentor_id = fields.Many2one('hr.hospital.doctor', string='Mentor')

    @api.onchange('is_intern')
    def _onchange_is_intern(self):
        if not self.is_intern:
            self.mentor_id = False


