# This is a generic Web Scraping script in Python 

# import librarys
import urllib2 
from bs4 import BeautifulSoup
import datetime
import csv

# specify a webpage
quote_page = 'https://www.greenentrepreneur.com/topic/growth-strategies'

# query the website and return the html code to the veriable 'page'
page = urllib2.urlopen(quote_page)

# parse the html page using Beautiful Soup nd store it in variable 'soup'
#soup = BeautifulSoup(page, 'html.parser')

# Use find() to search for the data you want to extract and store it in a variable
#<<strong class="symbolNum two" data-value="6277.02">
#article_link = soup.find('a', attrs = {'class': '/article/315458'})

# print data to screen
#print article_link
#price = price_box.text.strip() # strip() is used to remove starting and trailing

