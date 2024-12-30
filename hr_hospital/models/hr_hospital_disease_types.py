import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class HHDisease(models.Model):
    _name = 'hr.hospital.disease.types'
    _description = 'Disease'

    name = fields.Char()

    active = fields.Boolean(
        default=True,
    )