import matplotlib.pyplot as plt
import numpy as np
import string
from WordScrape import getword
from FactScrape import scrapelen
# Fixing random state for reproducibility


days = list(range(1,3))

daysx = []
numevents = []

for i in days:
	daysx.append(i)
	numevents.append(scrapelen("december",str(i)))

# test = string.ascii_letters
# test2 = test[0:9]
# x = ["test","test2"] #,3,4,5,6,7,8,10]
# y = [3,4]


# xy = (1,3)

# plt.scatter(x,y)

# for k,i,e in zip(test2,x,y):
# 	xy = (i,e)
# 	plt.annotate(k,xy)

# plt.show()

plt.hist(daysx,bins=5)
plt.show()
