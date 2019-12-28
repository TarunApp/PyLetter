import matplotlib.pyplot as plt
import numpy as np
import string
from WordScrape import getword
from FactScrape import scrapelen,numfacts
# Fixing random state for reproducibility


days = list(range(1,15))


def gevents(month, maindays):
	daysx = []
	numevents = []

	for i in maindays:
		daysx.append(i)
		numevents.append(numfacts(month,str(i)))

	return list(zip(daysx,numevents))
# print(gevents("December", days))
# print(gevents("March", days))


# x = [1,2,3,4,5,6]
# y = [3,4,1,2,8,10]

# # plt.scatter(x, y, color="blue") Organize points based on month, based on color



for i,e in gevents("December", days):
	plt.scatter(i, e, color="red", lable="December")
	xy = (i,e)
	plt.annotate("Dec. " + str(i), xy, wrap=True)

for i,e in gevents("March", days):
	plt.scatter(i, e, color="blue", lable="March")
	xy = (i,e)
	plt.annotate("Mar. " + str(i), xy, wrap=True)


# plt.title('Days')
# plt.legend()

plt.show()