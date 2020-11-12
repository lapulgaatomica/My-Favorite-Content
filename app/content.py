from . import app
from . import database
from .models import DailymailColumn
from .scraper import DailyMailColumns
from .email import send_email
from sqlalchemy.exc import IntegrityError

def get_dailymail_columns():	
	dailymail_columns = DailyMailColumns()
	for new_link, title, columnist in zip(dailymail_columns.links, dailymail_columns.titles, dailymail_columns.columnists):
		print(f'{new_link} scraped')
		with app.app_context():
			try:
				column = DailymailColumn(link=new_link, title=title, columnist=columnist)
				database.session.add(column)
				database.session.commit()
				send_email(app.config['MAIL_RECIPIENT'], 'New Dailymail Column', 'email/dailymail', link=new_link, title=title, columnist=columnist)
			except IntegrityError:
				# print(f'{new_link} has been saved before')
				database.session.rollback()