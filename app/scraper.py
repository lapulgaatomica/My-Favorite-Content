import requests
from bs4 import BeautifulSoup

class DailyMailColumns(object):
	"""
	Gets columns from dailymail.co.uk
	"""
	def __init__(self):
	    self.titles = []
	    self.columnists = []
	    self.links = []

	    self.get_columns()

	def get_columns(self):
		columns = requests.get('https://www.dailymail.co.uk/columnists/index.html')
		parsed_page = BeautifulSoup(columns.text, 'lxml')
		most_recent = parsed_page.find("div", {"class":"js-headers"}).find_all("div", {"class":"columnist-archive-content cleared link-ccox"})
		
		for column in most_recent:
		    link_and_title = column.find('h2', {'class':'linkro-ccox'})
		    self.columnists.append(column.find('a', {"class":"author"}).text)
		    self.titles.append(link_and_title.text)
		    self.links.append('https://www.dailymail.co.uk' + link_and_title.find('a')['href'])