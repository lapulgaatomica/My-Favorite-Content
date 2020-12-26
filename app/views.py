from flask import Blueprint, render_template, request
from .models import DailymailColumn

blue_print = Blueprint('views', __name__)

@blue_print.route('/')
def main():
	page = request.args.get('page', 1, type=int)
	pagination = DailymailColumn.query.paginate(page, per_page=10, error_out=False)
	columns = pagination.items
	return render_template('index.html', columns=columns, pagination=pagination)
