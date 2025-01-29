import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)

class HHDiagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    visit_id = fields.Many2one(
        comodel_name='hr.hospital.visits',
        string='Visit',
        required=True
    )

    disease = fields.Char(string='Disease', required=True)
    description = fields.Text(string='Description')
    approved = fields.Boolean(string='Approve', default = False)

