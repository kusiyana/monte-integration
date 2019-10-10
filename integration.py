#
# created by hayden 10-10-2019
# Script to perform ingegration of function using monte-carlo estimation
#
# Usage: alter function f_x with your chosen one. 

import random
import numpy as np
import matplotlib.pyplot as pyplot
from statistics import mean


# integration parameters
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def f_x(x):
	f_x = x**2 - 3*x +4 + x**3 - x**0.5 # adjust f_x here to integrate
	return f_x

end_point_x = 2 # provide x end point 
iteration_count = 1000 # number of iterations to get average over

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

end_point_f_x = f_x(end_point_x)
ratio = []
x_chosen = []
y_chosen = []
f_x_chosen = []
count = 0
hits = 0

def area(x, monte_ratio):
	area = f_x(x)*float(x) * float(monte_ratio)
	return area

random.seed(a=None)
for i in range(0,iteration_count):
	# chosen point
	x = end_point_x * random.random()
	y = end_point_f_x * random.random()
	x_chosen.append(x)
	y_chosen.append(y)
	f_x_chosen.append(f_x(x))
	if (f_x(x)) >= y:
		hits+=1
		if count > 0:
			ratio.append(float(hits)/float(count))
	count+=1

#print iteration_count, count

#print ratio[hits-10: hits]

print "Area is " + str(round(area(end_point_x, ratio[-1]),3))

#pyplot.plot(range(0,len(ratio)), ratio)
pyplot.scatter(x_chosen, f_x_chosen, alpha=0.1, s=2)
pyplot.scatter(x_chosen, y_chosen,alpha=0.2, s=1)
pyplot.show()


