import matplotlib.pyplot as plt
import numpy as np
import string
from WordScrape import getword
from FactScrape import scrapelen,numfacts
# Fixing random state for reproducibility


days = list(range(1,3))


def gevents(month, maindays):
	daysx = []
	numevents = []

	for i in maindays:
		daysx.append(i)
		numevents.append(numfacts(month,str(i)))

	return list(zip(daysx,numevents))
# print(gevents("December", days))
# print(gevents("March", days))

def graphevents(graph, month, maindays, plotcolor):
	for i,e in gevents(month, maindays):
		graph.scatter(i, e, color=plotcolor)
		xy = (i,e)
		graph.annotate("Dec. " + str(i), xy, wrap=True)


# x = [1,2,3,4,5,6]
# y = [3,4,1,2,8,10]

# # plt.scatter(x, y, color="blue") Organize points based on month, based on color



# for i,e in gevents("December", days):
# 	plt.scatter(i, e, color="red", lable="December")
# 	xy = (i,e)
# 	plt.annotate("Dec. " + str(i), xy, wrap=True)

# for i,e in gevents("March", days):
# 	plt.scatter(i, e, color="blue", lable="March")
# 	xy = (i,e)
# 	plt.annotate("Mar. " + str(i), xy, wrap=True)

fig, (ax, ax2) = plt.subplots(2,1)
graphevents(ax, "December", days, "red")
graphevents(ax2, "March", days, "blue")

# plt.title('Days')
# plt.legend()
# ax.set_title('testero')
# ax2.set_title('testero - 2')


plt.tight_layout()
plt.show()