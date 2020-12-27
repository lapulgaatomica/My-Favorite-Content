from . import database as db
from datetime import datetime

class DailymailColumn(db.Model):
	__tablename__ = 'dailymail_columns'
	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String, nullable=False, unique=True, index=True)
	title = db.Column(db.String, nullable=False)
	columnist = db.Column(db.String, nullable=False)
	date_added = db.Column(db.DateTime(), default=datetime.now)

	@staticmethod
	def add_a_past_date():
		i = 0
		for dailymail_column in DailymailColumn.query.all():
			if not dailymail_column.date_added:
				dailymail_column.date_added = datetime(2020, 12, 25, 0, 0, 0, i)
				db.session.add(dailymail_column)
				db.session.commit()
				i += 1

	def __repr__(self):
		return f'<{self.id} : {self.title}>'
