from openerp.osv import fields, osv

class hold_membership(osv.Model):
	_name = "hold.membership"
	_coloums = {
		'reason_hold' : fields.char('Reason'),
		'hold_start': fields.datetime('Start Date'),
		'hold_end': fields.datetime('End Date'),
		'hold_fee': fields.char('Hold Fee'),
	}
hold_membership()