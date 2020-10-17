from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_mail import Mail
import atexit


database = SQLAlchemy()
mail = Mail()
app = Flask(__name__)

def scrape_dailymail():
	from .models import DailymailColumn
	from .scraper import DailyMailColumns
	from .email import send_email
	from sqlalchemy.exc import IntegrityError

	dailymail_columns = DailyMailColumns()
	for new_link, title, columnist in zip(dailymail_columns.links, dailymail_columns.titles, dailymail_columns.columnists):
		with app.app_context():
			try:
				column = DailymailColumn(link=new_link, title=title, columnist=columnist)
				database.session.add(column)
				database.session.commit()
				send_email(app.config['MAIL_RECIPIENT'], 'New Dailymail Column', 'email/dailymail', link=new_link, title=title, columnist=columnist)
			except IntegrityError:
				# print(f'{new_link} has been saved before')
				database.session.rollback()

def create_app(config_name):
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	database.init_app(app)
	mail.init_app(app)

	if app.config['SSL_REDIRECT']:
	    from flask_sslify import SSLify
	    sslify = SSLify(app)

	from apscheduler.schedulers.background import BackgroundScheduler
	# scrape_dailymail()
	# Create a schedule to run the scrape_news function in the background
	scheduler = BackgroundScheduler()
	scheduler.add_job(func=scrape_dailymail, trigger="interval", seconds=60)
	# Starts the schedule
	scheduler.start()

	# Shuts down scheduler before file exists
	atexit.register(lambda: scheduler.shutdown())

	return app
