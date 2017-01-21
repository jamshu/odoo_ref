# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import Warning

class Session(models.Model):
    _name = 'openacademy.session'
    
    name = fields.Char(required=True)
    state = fields.Selection([('draft', 'Draft'),('confirm', 'Confirm'),('cancel', 'Cancel'),('done', 'Done')], required=True, default='draft')
    duration = fields.Float()
    seats = fields.Integer()
    start_date =  fields.Date()
    active =  fields.Boolean(default=True)
    description =  fields.Text()
    course = fields.Many2one('openacademy.course')
    instructor = fields.Many2one('res.partner')
    attendees = fields.Many2many('res.partner')
    occupation = fields.Float(compute="calculate_occupation")
    course_info = fields.Text(related="course.description")

    @api.onchange('course')
    def onchange_course(self):
        if self.course and not self.name:
            self.name = self.course.name + ' Session'

    @api.constrains('attendee','instructor')
    def attendee_constrains(self):
        if self.instructor.id in self.attendees.ids:
            raise Warning('You can not add instructor as a attendee')
    
    @api.multi
    @api.depends('seats','attendees')
    def calculate_occupation(self):
        for rec in self:
            if rec.seats:
                rec.occupation =  len(rec.attendees) * 100 / rec.seats
            else:
                rec.occupation = 0
    
    
    @api.one 
    def unlink(self):
        if self.state != 'draft':
            raise Warning("You Can Only Delete Draft Record")
    @api.one
    def do_confirm(self):
        self.state = 'confirm'

    @api.one
    def do_done(self):
        self.state = 'done'

    @api.one
    def do_cancel(self):
        self.state = 'cancel'

    @api.one
    def do_reset(self):
        self.state = 'draft'

