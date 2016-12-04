#This file includes tasks from Chapter 3.11

from vec import Vec
from vecutil import *

def triangle_solve_n(rowlist, b):
	D = rowlist[0].D
	n = len(D)
	assert D == set(range(n))

	x = zero_vec(D)
	for i in reversed(range(n)):
		x[i] = (b[i]  - rowlist[i] * x) / rowlist[i][i]
	return x

def Excercis_3_11_4():
	rowlist = [
	list2vec([2,3,-4]),
	list2vec([0,1,2]),
	list2vec([0,0,5]),
	]
	b = [10,3,15]
	x = triangle_solve_n(rowlist,b)
	print(x)

Excercis_3_11_4()