from flask import Blueprint, render_template
from .models import DailymailColumn

blue_print = Blueprint('views', __name__)

@blue_print.route('/')
def main():
	columns = DailymailColumn.query.all()
	return render_template('index.html', columns=columns)