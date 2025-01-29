import logging

from odoo import models, fields, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HHVisit(models.Model):
    _name = 'hr.hospital.visits'
    _description = 'Visits'

    name = fields.Char()

    active = fields.Boolean(
        default=True
    )


    doctor_id = fields.Many2one(
        comodel_name = 'hr.hospital.doctor',
        string = 'Doctor',
    )


    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
    )

    visit_date = fields.Datetime(string='Visit date', required=True)

    status = fields.Selection(
        selection=[
            ('scheduled', 'заплановано'),
            ('completed', 'Завершено'),
            ('canceled', 'Скасовано')
        ],
        string='Статус візиту',
        default='scheduled'
    )

    scheduled_date = fields.Datetime(string='Запланована дата та час візиту')
    actual_date = fields.Datetime(string='Дата та час, коли відбувся візит')

    diagnosis_ids = fields.One2many(
        comodel_name='hr.hospital.diagnosis',
        inverse_name='visit_id',
        string="Diagosis"
    )

    @api.constrains('scheduled_date', 'actual_date', 'doctor_id')
    def _check_edit_restrictions(self):
        for visit in self:
            if visit.status == 'completed' and self.env.user.has_group('base.group_user'):
                raise ValidationError('the visit has already taken place')

    @api.constrains('patient_id', 'doctor_id', 'scheduled_date')
    def _check_duplicate_visit(self):
        for visit in self:
            if visit.patient_id and visit.doctor_id and visit.scheduled_date:
                start_of_day = fields.Datetime.to_string(fields.Datetime.context_timestamp(
                    visit, fields.Datetime.from_string(visit.scheduled_date).replace(hour=0, minute=0, second=0)
                ) )
                end_of_day = fields.Datetime.to_string(fields.Datetime.context_timestamp(
                    visit, fields.Datetime.from_string(visit.scheduled_date).replace(hour=23, minute=59, second=59)
                ))

                overlapping_visits = self.env['hr.hospital.visits'].search_count([
                    ('id', '!=', visit.id),
                    ('doctor_id', '=', visit.doctor_id.id),
                    ('patient_id', '=', visit.patient_id.id),
                    ('scheduled_date', '>=', start_of_day),
                    ('scheduled_date', '<=', end_of_day),
                    ('status', '!=', 'canceled')
                ])

                if overlapping_visits > 0:
                    raise ValidationError("The patient is already booked with a doctor for that day")

    def unlink(self):
        for visit in self:
            if visit.diagnosis_ids:
                raise ValidationError("You can delete a visit that has diagnoses")
            return super(HHVisit, self).unlink()

    def action_archive(self):
        for visit in self:
            if visit.diagnosis_ids:
                raise ValidationError("There is a diagnosis in the visit")
            return super(HHVisit, self).write({'active': False})

    def action_confirm(self):
        self.write({'status': 'completed', 'actual_date': fields.Datetime.now()})

    def action_cancel(self):
        self.write({'status': 'canceled'})

