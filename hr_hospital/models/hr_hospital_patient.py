import logging

from odoo import models, fields, api
from datetime import date

_logger = logging.getLogger(__name__)

class HHPatient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = 'hr_hospital_person'
    _description = 'Patient'

    name = fields.Char()

    active = fields.Boolean(
        default = True
    )

    personal_doctor = fields.Many2one('hr.hospital.doctor', string='Personal Doctor')
    birth_date = fields.Date(string='Birthdate')
    passport_data = fields.Char(string='Passport')
    emergency_contact = fields.Char(string='Contact')

    age = fields.Integer(string='Вік', compute='_compute_age', store=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                birth_date = fields.Date.from_string(record.birth_date)
                record.age = today.year - birth_date.year - (
                            (today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                record.age = 0

    def action_open_change_doctor_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Change Doctor',
            'res_model': 'hr.hospital.change.doctor',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_ids': self.ids},
        }
