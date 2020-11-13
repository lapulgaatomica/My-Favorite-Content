from . import database as db

class DailymailColumn(db.Model):
	__tablename__ = 'dailymail_columns'
	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String, nullable=False, unique=True)
	title = db.Column(db.String, nullable=False)
	columnist = db.Column(db.String, nullable=False)

	def __repr__(self):
		return f'<{self.id} : {self.title}>'