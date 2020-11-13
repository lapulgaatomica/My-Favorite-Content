from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_mail import Mail
import atexit
from apscheduler.schedulers.background import BackgroundScheduler


database = SQLAlchemy()
mail = Mail()
app = Flask(__name__)

def create_app(config_name):
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	database.init_app(app)
	mail.init_app(app)

	if app.config['SSL_REDIRECT']:
		#used when the app is on heroku to secure the requests passed by
		#users and prevent their credentials from being intercepted by a
		#malicious third party
	    from flask_sslify import SSLify
	    sslify = SSLify(app)

	from .content import get_dailymail_columns
	scheduler = BackgroundScheduler()
	# Create a schedule to run the get_dailymail_columns function in the background
	scheduler.add_job(func=get_dailymail_columns, trigger="interval", seconds=10)
	# Starts the schedule
	scheduler.start()

	# Shuts down scheduler before file exists
	atexit.register(lambda: scheduler.shutdown())

	return app
