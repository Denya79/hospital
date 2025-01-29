import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class HHDoctorChange(models.TransientModel):
    _name = 'hr.hospital.change.doctor'
    _description = 'Wizzard for change Doctor'

    doctor_id = fields.Many2one('hr.hospital.doctor', string='New doctor', required=True)
    def action_change_doctor(self):
        active_ids = self.env.context.get('active_ids')
        patients = self.env['hr.hospital.patient'].browse(active_ids)
        for patient in patients:
            patient.personal_doctor = self.doctor_id