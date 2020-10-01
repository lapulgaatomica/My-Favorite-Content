from . import main
from .scraper import DailyMailColumns
from flask import render_template

@main.route('/', methods=['GET'])
def index():
	dailymail_columns = DailyMailColumns()
	content = {'titles' : dailymail_columns.titles, 'columnists' : dailymail_columns.columnists, 'links' : dailymail_columns.links}
	# return render_template('index.html', content=content)
	return content