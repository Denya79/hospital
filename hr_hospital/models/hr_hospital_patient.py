import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class HHPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char()

    active = fields.Boolean(
        default = True
    )