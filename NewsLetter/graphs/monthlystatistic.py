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

	return zip(daysx,numevents)
# print(gevents("December", days))
# print(gevents("March", days))

def graphevents(graph, month, maindays, plotcolor="red"):
	for i,e in gevents(month, maindays):
		graph.scatter(i, e, color=plotcolor, label=month)
		xy = (i,e)
		# graph.annotate("Dec. " + str(i), xy, wrap=True)


# x = [1,2,3,4,5,6]
# y = [3,4,1,2,8,10]

# # plt.scatter(x, y, color="blue") Organize points based on month, based on color



# for i,e in gevents("December", days):
# 	plt.scatter(i, e, color="red")
# 	xy = (i,e)
# 	plt.annotate("Dec. " + str(i), xy, wrap=True)

# for i,e in gevents("March", days):
# 	plt.scatter(i, e, color="blue")
# 	xy = (i,e)
# 	plt.annotate("Mar. " + str(i), xy, wrap=True)

k = gevents("December", days)
x, y = zip(*k)
print(y)
#faster compile time
fig, (ax) = plt.subplots(1,1)
ax.scatter(x,y)


# graphevents(ax2, "March", days, "blue")

# ax.plot()

# plt.title('Days')
# ax.set_title('testero')
# ax2.set_title('testero - 2')


# plt.tight_layout()
plt.show()