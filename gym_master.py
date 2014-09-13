from openerp.osv import fields, osv

class gym_member(osv.Model):
	_name = "gym.member"
	_inherit = 'hr.employee'
	_columns = {
		'membership_line': fields.one2many('gym.membership', 'membership'),
		'booking_line': fields.one2many('gym.booking', 'booking'),
	}
gym_member()

class gym_membership(osv.Model):
	_name = "gym.membership"
	_columns = {
		'membership' : fields.many2one('gym.member',readonly=True),
		'program_group' : fields.selection([('Gym Membership','Gym Membership'),('Group Activity','Group Activity'),('Club','Club')],'Program Group'),
		'Program' : fields.selection([('12 Month','12 Month'),('6 Month','6 Month'),('3 Month','3 Month'),('1 Month','1 Month'),('Weekly','Weekly')],'Program'),
		'Program_price' : fields.integer('Program Price'),
		'start_date' : fields.datetime('Start Date'),
		'end_date':fields.datetime('End Date'),
		'sign_up' : fields.char('SignUp Fee'),
		'visit' : fields.integer('No of Visit'),
	}
gym_membership()

class card_detail(osv.Model):
	_name = 'card.detail'
	_columns = {
		'card_number' : fields.integer("Card Number"),
	}
card_detail()

class gym_booking(osv.Model):
	_name = 'gym.booking'
	_description = 'Gym Booking'
	_columns = {
		'name': fields.char('Subject', required=True, select=1),
		'user_id': fields.many2one('gym.member', 'Member'),
		'booking' : fields.many2one('gym.member',readonly=True),
		'date_action': fields.date('Next Action Date', select=True),
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

class gym_measurment(osv.Model):
	_name = 'gym.measurment'
	_columns = {
		'date' : fields.date('Date'),
		'factor_id' : fields.many2many('Measurment Factor'),
		'current_goal' : fields.char('Current Goal'), 
	}
gym_measurment()

class measurment_factor(osv.Model):
	_name = 'measurment.factor'
	_columns = {
		'member_id': fields.many2one('gym.member','Member Name'),
		'date' : fields.date('Date'),
		'factor_name': fields.char('Factor Name'),
		'factor_value' : fields.char('Factor Value'),
	}
measurment_factor()