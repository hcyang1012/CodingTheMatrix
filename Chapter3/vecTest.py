from vec import Vec

print("Setter and Getter Test")
newVec = Vec({'A','B','C'},{'A':1.0})
print(newVec['A'])
print(newVec['B'])
newVec['C'] = 5.0
print(newVec['C'])
newVec['B'] = newVec['C'] = 6.0
print(newVec['B'])
print(newVec['C'])



print("Equal operation test")
print(Vec({'a', 'b', 'c'}, {'a':0}) == Vec({'a', 'b', 'c'}, {'b':0})) #T
print(Vec({'a', 'b', 'c'}, {'a': 0}) == Vec({'a', 'b', 'c'}, {})) #T
print(Vec({'a', 'b', 'c'}, {}) == Vec({'a', 'b', 'c'}, {'a': 0})) #T
print(Vec({'x','y','z'},{'y':1,'x':2}) == Vec({'x','y','z'},{'y':1,'z':0})) #F
print(Vec({'a','b','c'}, {'a':0,'c':1}) == Vec({'a','b','c'}, {'a':0,'c':1,'b':4})) #F
print(Vec({'a','b','c'}, {'a':0,'c':1,'b':4}) == Vec({'a','b','c'}, {'a':0,'c':1})) #F
print(Vec({'a','b'},{'a':1}) == Vec({'a','b'},{'b':1})) #F
print(Vec({'a','b'},{'a':1}) == Vec({'a','b'},{'a':2})) #F


print("Add operation test")
a = Vec({'a','e','i','o','u'}, {'a':0,'e':1,'i':2})
b = Vec({'a','e','i','o','u'}, {'o':4,'u':7})
c = Vec({'a','e','i','o','u'}, {'a':0,'e':1,'i':2,'o':4,'u':7})
print(a + b == c)

print("Dot operation test")
u1 = Vec({'a','b'}, {'a':1, 'b':2})
u2 = Vec({'a','b'}, {'b':2, 'a':1})
print(u1*u2) #5
print(u1 == Vec({'a','b'}, {'a':1, 'b':2})) #True
print(u2 == Vec({'a','b'}, {'b':2, 'a':1})) #True

v1 = Vec({'p','q','r','s'}, {'p':2,'s':3,'q':-1,'r':0})
v2 = Vec({'p','q','r','s'}, {'p':-2,'r':5})
print(v1*v2) #-4

w1 = Vec({'a','b','c'}, {'a':2,'b':3,'c':4})
w2 = Vec({'a','b','c'}, {'a':12,'b':8,'c':6})
print(w1*w2) #72


v1 = Vec({1, 2}, {1 : 3, 2 : 6})
v2 = Vec({1, 2}, {1 : 2, 2 : 1})
print(v1 * v2) #12



print("Scalar mul operation test")
zero = Vec({'x','y','z','w'}, {})
u = Vec({'x','y','z','w'},{'x':1,'y':2,'z':3,'w':4})
print(0*u == zero) #True
print(1*u == u) #True
print(0.5*u == Vec({'x','y','z','w'},{'x':0.5,'y':1,'z':1.5,'w':2})) #True
print(u == Vec({'x','y','z','w'},{'x':1,'y':2,'z':3,'w':4})) #True