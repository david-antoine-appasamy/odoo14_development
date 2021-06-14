from odoo import api, fields, models


class StudentRecord(models.Model):
    _inherit = 'res.config.settings'
    _name = "student.student"
    name = fields.Char(string='Name', required=True)
    middle_name = fields.Char(string='Middle Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    photo = fields.Binary(string='Photo')
    student_age = fields.Integer(string='Age')
    student_dob = fields.Date(string="Date of Birth")
    student_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    student_address = fields.Char(string='Address')
    student_contactno=fields.Char(string='Contact No')
    student_email=fields.Char(string='Email')
    student_active=fields.Boolean(string='Active',default=True)
    student_information=fields.Text(string='Student Information')
    student_fees=fields.Float(string='Student Fees',digits=(6,2),required=True, help="Enter the Fees")
    nationality = fields.Many2one('res.country', string='Nationality')
    language=fields.Many2many('res.lang',string='Language')
    currency=fields.Many2many('res.currency',string='Currency')
    partner=fields.Many2one('res.partner',string='Partner')
    user=fields.Many2many('res.users',string='Users')
    attendee_ids=fields.Many2many('res.partner',string="Attendees")
    rel_id = fields.One2many('child.child', 'parent_field_id', string='Child IDS')

    class studentchild(models.Model):
        _name = 'child.child'
        allied_partner = fields.Char(string="Allied Partner")
        desc = fields.Char(string="Description")
        parent_field_id = fields.Many2one('res.partner', string='Parent ID')




