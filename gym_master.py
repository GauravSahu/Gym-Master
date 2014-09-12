from openerp.osv import fields, osv

class gym_member(osv.Model):
	_name = "gym.member"
	_inherit = 'hr.employee'
	_columns = {
		'membership_line': fields.one2many('gym.membership', 'membership'),
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