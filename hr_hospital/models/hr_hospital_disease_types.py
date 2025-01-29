import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class HHDisease(models.Model):
    _name = 'hr.hospital.disease.types'
    _description = 'Disease'
    _parent_store = True

    name = fields.Char()
    active = fields.Boolean(
        default=True,
    )
    parent_id = fields.Many2one(
        'hr.hospital.disease.types',
        string='Parent Disease',
        ondelete='cascade'
    )
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many(
        'hr.hospital.disease.types',
        'parent_id',
        string='Child Diseases'
    )