import matplotlib.pyplot as plt
import numpy as np
import string
from WordScrape import getword
from FactScrape import scrapelen,numfacts
# Fixing random state for reproducibility


days = list(range(1,3))
non_numerical = ["December", "March"]

def gevents(month, maindays):
	"""Return a list of events for given month and list of days"""


	daysx = []
	numevents = []

	for i in maindays:

		daysx.append(i)
		numevents.append(numfacts(month,str(i)))

	return zip(daysx,numevents)

def graphevents(graph, month, maindays, plotcolor="red"):
	"""Annotate plotted points on graph"""
	for i,e in gevents(month, maindays):
		graph.scatter(i, e, color=plotcolor, label=month)
		xy = (i,e)
		# graph.annotate("Dec. " + str(i), xy, wrap=True)

def plot_scatter(graph, month, data, color="red"):
	plot_data = gevents(month, data)
	x, y = zip(*plot_data)
	result = graph.scatter(x,y, label=month)
	return result

def plot_bar(graph, month, data, color="blue"):
	plot_data = gevents(month, data)
	x, y = zip(*plot_data)
	del x
	const_x = [month] * len(y)
	result = graph.bar(const_x,sum(y), label=month)
	plt.annotate(str(sum(y)), (const_x, sum(y)))
	# graph.annotate()
	return result

# testdata = gevents("December", days)
# x, y = zip(*testdata)
# print(x,y)



fig, (ax) = plt.subplots(1,1)

plt.show()