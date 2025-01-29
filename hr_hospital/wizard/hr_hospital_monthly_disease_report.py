import logging
from odoo import models, fields, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class HHMonthlyDiseaseReportWizard(models.TransientModel):
    _name = 'hr.hospital.monthly.disease.report'
    _description = 'Monthly Disease Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date',required=True)
    doctor_ids = fields.Many2many('hr.hospital.doctor', string='Doctors')
    disease_ids = fields.Many2one('hr.hospital.disease.types', string='Diseases',required=True)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise ValidationError('Error in Start and End date')

    def action_generate_report(self):
        domain = [
            ('date_diagnosed', '>=', self.start_date),
            ('date_diagnosed', '<=', self.end_date)
        ]
        if self.doctor_ids:
            domain.append(('doctor_id', 'in', self.doctor_ids.ids))

        if self.disease_ids:
            domain.append(('disease_id', 'in', self.disease_ids.ids))

        diagnoses = self.env['hr.hospital.diagnosis'].search(domain)

        _logger.info(f"Generated report with {len(diagnoses)} diagnoses matching criteria")

        return {
            'type': 'ir.actions.act_window',
            'name': 'Monthly Disease Report',
            'res_model': 'hr.hospital.diagnosis',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', diagnoses.ids)],
            'context': self.env.context,
        }