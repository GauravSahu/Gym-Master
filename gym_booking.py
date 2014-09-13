from openerp.osv import fields, osv

class gym_booking(osv.Model):
	_name = 'gym.booking'
	_description = 'Gym Booking'
	_columns = {
		'membership' : fields.many2one('gym.member',readonly=True),
		'booking_date' : fields.datetime('Booking Date'),
		'booking_time' : fields.char('Booking Time'),
		'end_time' : fields.datetime('End Time'),
		'start_time' : fields.datetime('Start Date'),
		'resource' : fields.char('Resource'),
		'booking_type' : fields.selection([('First Assesment','First Assesment'),('Re Assesment','Re Assesment'),('Measurment','Measurment'),('Trial','Trial')],'Booking Type'),
		'notes' : fields.char('Notes'),
		'state': fields.selection([('Open','Open'),('Confirmed','Confirmed')]),
	}
gym_booking()

