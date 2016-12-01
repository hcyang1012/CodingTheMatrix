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

def Excercise3_6_1():
    w = [5-2,7-3]
    x = [2,3]

    u = [2,3]
    v = [5,7]
    plot([add2(scalar_vector_multi(i/100.,w),x) for i in range(101)], 10)
    plot([u,v],10)


def segment(pt1, pt2):
    return [add2(scalar_vector_multi(i/100,pt1),scalar_vector_multi((1-(i/100)),pt2)) for i in range(101)]

def Task_3_6_9():
    plot([[3.5,3],[0.5,1]],10)
    plot(segment([3.5,3],[0.5,1]),10)


class Vec:
    def __init__ (self,labels,function):
        self.D = labels;
        self.f = function;

    #def __init__ (self,labels):
    #    self.D = labels;
    #    self.f = {}
    #    self.zero_init();

    def zero_init(self):
        for d in self.D:
            self.f[d] = 0

def zero_vec(D):
    return (Vec(D,{}));

def Quiz_3_7_1():
    vec = zero_vec(['A','B','C']);
    print (vec.f)

def setitem(v, d, val):
    v.f[d] = val;

def getitem(v,d):
    if d in v.f:
        return v.f[d]
    else:
        return 0

def Quiz_3_7_2():
    vec = zero_vec(['A','B','C']);
    setitem(vec,'A',1)
    print(getitem(vec,'A'))

def scalar_mul(v,alpha):
    return Vec(v.D, {d:alpha*value for d,value in v.f.items()})

def Quiz_3_7_3():
    vec = zero_vec(['A','B','C']);
    setitem(vec,'A',1)
    print(scalar_mul(vec,2).f)


def add(u,v):
    return Vec(u.D, {d:getitem(u,d) + getitem(v,d) for d in u.D})

def Quiz_3_7_4():
    v = Vec({'A','B','C'},{'A':1}) 
    u = Vec(v.D,{'A':5,'C':10})
    print(add(u,v).f)

def neg(v):
    return scalar_mul(v,-1)

def Quiz_3_7_5():
    v = Vec({'A','B','C'},{'A':1, 'B':0, 'C':2}) 
    print(neg(v).f)

# Task_3_3_3();
# Task_3_4_3();
# Prob3_4_4();
# Quiz_3_5_3();
# Excercise3_6_1();
# Task_3_6_9()
# Quiz_3_7_1()
# Quiz_3_7_2()
# Quiz_3_7_3()
# Quiz_3_7_4()
Quiz_3_7_5()

## A dummy code to wait for end command.
#while(True):
#	A = 1;
