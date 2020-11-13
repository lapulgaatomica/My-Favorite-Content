from . import app
from . import database
from .models import DailymailColumn
from .scraper import DailyMailColumns
from .email import send_email
from sqlalchemy.exc import IntegrityError

def get_dailymail_columns():
	"""
    calls the DailyMailColumns scraper and saves
    the new ones to the database 

    :return: None
    """
	dailymail_columns = DailyMailColumns()
	for new_link, title, columnist in zip(dailymail_columns.links, dailymail_columns.titles, dailymail_columns.columnists):
		with app.app_context():
			try:
				column = DailymailColumn(link=new_link, title=title, columnist=columnist)
				database.session.add(column)
				database.session.commit()
				send_email(app.config['MAIL_RECIPIENT'], 'New Dailymail Column', 'email/dailymail', link=new_link, title=title, columnist=columnist)
			except IntegrityError:
				database.session.rollback()