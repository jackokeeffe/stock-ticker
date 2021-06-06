'''
    PROJECT  : Project 2.7. Long ISP: The Stock Market Ticker
    PURPOSE  : Search for stock info based on given tickers (through GUI)
    DATE     : 2021 05 29
    MCU      : 328P
    STATUS   : Working
    NOTES    : Comments not on code line reference to the line below
    REFERENCE: http://darcy.rsgc.on.ca/ACES/TEI3M/2021/ISPs.html
'''
from urllib.request import urlopen # Used for Managing URLS
from bs4 import BeautifulSoup      # Allows me to view HTML data

def search(ticker):
	url = "https://finance.yahoo.com/quote/" + ticker # Specific link for given ticker
	page = urlopen(url)                               # Open URL
	html = page.read().decode("utf-8")                # Decode page using UTF-8 encoding
	soup = BeautifulSoup(html, "html.parser")         # Set HTML data to soup
	try:
		# Searches for stock symbol by looking for h1 with given class
		symbol = str(soup.find('h1', {'class': 'D(ib) Fz(18px)'})).split('>')\
			[1].split('</')[0].split("(")[1].split(')')[0]
		# Searches for current price using the same method
		current_price = str(soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}))\
			.split(">")[1].split("</")[0]
		# Searches for percent gains using the same method
		percent_gains = str(soup.find('div', {'class': 'D(ib) Mend(20px)'})).split('data-reactid="33">')\
			[1].split('<')[0]
		all_info = symbol + ": " + current_price + " | " + percent_gains # Turns all info found into one given string
		return all_info # Return all_info so that it can be sent to Arduino
	except:
		return url.split("/quote/")[1] + " is not a valid ticker" # If ticker does not exist, tell user