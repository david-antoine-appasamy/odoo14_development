from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _rec_name = 'name'
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _description = "Hospital Patient Details"

    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    state=fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'),
                            ('cancel', 'Cancel')], default='draft', string="Status")

