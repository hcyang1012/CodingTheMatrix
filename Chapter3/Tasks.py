from plotting import *

def add2(v,w):
    return [v[0] + w[0],v[1] + w[1]]

def addn(v,w):
    return [x+y for(x,y) in zip(v,w)]

def scalar_vector_multi(alpha, v):
    return [alpha * v[i] for i in range(len(v))]

def Task_3_3_3():
	L = [[2,2], [3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75, 1], [3,1], [3.25, 1]]
	plot(L,4);

def Task_3_4_3():
    L = [[2,2], [3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75, 1], [3,1], [3.25, 1]]
    plot([add2(v,[1,2]) for v in L],4);

def Prob3_4_4():
    L = [[2,2], [3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75, 1], [3,1], [3.25, 1]]
    plot([addn(v,[1,2]) for v in L], 4);

def Quiz_3_5_3():
    L = [[2,2], [3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75, 1], [3,1], [3.25, 1]]
    plot([scalar_vector_multi(2,v) for v in L],10);


# Task_3_3_3();
# Task_3_4_3();
# Prob3_4_4();
Quiz_3_5_3();

## A dummy code to wait for end command.
while(True):
	A = 1;