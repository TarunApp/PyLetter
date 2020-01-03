import csv
from FactScrape import getfact, scrapelen, numfacts

def gevents(month, day):
	return numfacts(month, str(day))

# days = range(1,3)
# x = gevents("December",days)
# print(x)

def foo():
	return ["December"]

#Make into function
with open('asd.csv', mode='w', newline='') as filedata:
	maintest = csv.writer(filedata, delimiter=',')
	maintest.writerow(["Month", "Day", "Events"])
	days = range(1,10)
	#example inputs
	months = ["January", "March"]
	for i in months:
		for e in days:
			maintest.writerow([i, e, numfacts(i,str(e))])


#Test for proper format
# import pandas as pd

# x = pd.read_csv('test.csv')

# print(x.describe)