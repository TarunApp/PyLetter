import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import string
from WordScrape import getword

def parsetotext(foundsoup):
	k = []
	for child in foundsoup:
		k.append(child)
	l = k[1]
	i = l.strip(' ')
	rcb = []
	for zx in k[0]:
		rcb.append(zx)
	return rcb[0]+"-"+i

def getfact(month, day):
	url = "https://www.timeanddate.com/on-this-day" + "/" + month + "/" + day

	request = requests.get(url)		#<---------- Move this into a seperate function
	html_content = request.text

	soup = BeautifulSoup(html_content, "html.parser")

	#Find the tag and its attribute
	x = soup.find("h3", class_ ='otd-ttl')
	y = x.find_next("h3", class_ ='otd-ttl')
	g = y.find_next("h3", class_='otd-ttl')
	h = g.find_next("h3", class_ = 'otd-ttl')
	e = h.find_next("h3", class_ = 'otd-ttl')
	# print(type(x))

	month = "december"
	day = "12"
	url = "https://www.timeanddate.com/on-this-day" + "/" + month + "/" + day

	request = requests.get(url)		#<---------- Move this into a seperate function
	html_content = request.text

	soup = BeautifulSoup(html_content, "html.parser")

	x = soup.find("div",{"class" : "eight columns" })

	y = x.find("h3", class_= "otd-cat")



def scrapelen(month,day):
	url = "https://www.timeanddate.com/on-this-day" + "/" + month + "/" + day

	request = requests.get(url)		#<---------- Move this into a seperate function
	html_content = request.text

	soup = BeautifulSoup(html_content, "html.parser")

	x = soup.find("div",{"class" : "eight columns" })

	# print(x)
	y = x.find_all("h3", class_ = "otd-ttl")
	# print(y)

	return len(y)

print(scrapelen("march", "12"))