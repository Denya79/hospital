import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)

class Person(models.AbstractModel):
    _name = 'hr_hospital_person'
    _description = 'Person'

    first_name = fields.Char(string='First name', required=True)
    last_name = fields.Char(string='Last name', required=True)
    phone = fields.Char(string='Phone')
    photo = fields.Image(max_width=512, max_height=512,)
    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        string='Gender', default='male'
    )
