import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import string
import random



def getword(year,month,day):
	#year = ""
	#month = ""
	#day = ""

	functionyear = str(year)
	functionmonth = str(month)
	functionday = str(day)


	url2 = "https://www.wordnik.com/word-of-the-day/"+functionyear+"/"+functionmonth+"/"+functionday
	request2 = requests.get(url2)
	html_content2 = request2.text
	soup = BeautifulSoup(html_content2, "html.parser")
		
	word = soup.find("h1")
	n = word.text


	e = soup.find("div", class_="word-module module-definitions")
	definition = e.find("li")
	k = definition.text

	l = list(definition)
	i = l[0]
	#print(i)
	h = list(i)
	maindef = l[1]



	return string.capwords(n) + "-"+ "[" +h[0]+ "]"+maindef


# print(getword(2018,3,2))