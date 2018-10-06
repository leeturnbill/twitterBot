# This is a generic Web Scraping script in Python 

# import librarys
import urllib2 
from bs4 import BeautifulSoup
import datetime
import csv

# specify a webpage
quote_page = 'https://info.binance.com/en/currencies/bitcoin'

# query the website and return the html code to the veriable 'page'
page = urllib2.urlopen(quote_page)

# parse the html page using Beautiful Soup nd store it in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Use find() to search for the data you want to extract and store it in a variable
#<<strong class="symbolNum two" data-value="6277.02">
price_box = soup.find('strong', attrs = {'class': 'symbolNum two'})

# print data to screen
price = price_box.text.strip() # strip() is used to remove starting and trailing
print datetime.datetime.now()
print '$' + price

# save data to a csv file
