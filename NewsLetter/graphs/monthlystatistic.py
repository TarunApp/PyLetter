import matplotlib.pyplot as plt
import numpy as np
import string
from WordScrape import getword
from FactScrape import scrapelen,numfacts
# Fixing random state for reproducibility


days = list(range(1,2))

daysx = []
numevents = []

for i in days:
	daysx.append(i)
	numevents.append(numfacts("December",str(i)))


plt.scatter(daysx, numevents)

for i,e in zip(daysx, numevents):
	xy = (i,e)
	plt.annotate("December " + str(i), xy)


plt.show()
