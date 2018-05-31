# -*- coding: utf-8 -*-

# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
rankings = 'https://basketballmonster.com/PlayerRankings.aspx'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(rankings)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# find the elements
container = soup.find('div', attrs={'class': 'results-table'})
rows = container.findAll('tr')

# construct stats array
stats = []
for i in xrange(1, len(rows)):
	stats.append(rows[i].findAll('td'))

rowLen = len(stats[1])

for i in xrange(1, len(stats)):
	for j in xrange(1, rowLen):
		if stats[i]:
			stats[i][j] = str(stats[i][j].text.strip())

print stats