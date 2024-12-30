import logging


from odoo import models, fields

_logger = logging.getLogger(__name__)


class HHVisit(models.Model):
    _name = 'hr.hospital.visits'
    _description = 'Visits'

    name = fields.Char()

    active = fields.Boolean(
        default=True
    )


    doctorId = fields.Many2one(
        comodel_name = 'hr.hospital.doctor',
        string = 'Doctor',
    )


    patientId = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
    )

    visit_date = fields.Datetime()