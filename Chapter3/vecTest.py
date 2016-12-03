from vec import Vec

newVec = Vec({'A','B','C'},{'A':1.0})
print(newVec['A'])
print(newVec['B'])
newVec['C'] = 5.0
print(newVec['C'])
newVec['B'] = newVec['C'] = 6.0
print(newVec['B'])
print(newVec['C'])




print(Vec({'a', 'b', 'c'}, {'a':0}) == Vec({'a', 'b', 'c'}, {'b':0})) #T
print(Vec({'a', 'b', 'c'}, {'a': 0}) == Vec({'a', 'b', 'c'}, {})) #T
print(Vec({'a', 'b', 'c'}, {}) == Vec({'a', 'b', 'c'}, {'a': 0})) #T
print(Vec({'x','y','z'},{'y':1,'x':2}) == Vec({'x','y','z'},{'y':1,'z':0})) #F
print(Vec({'a','b','c'}, {'a':0,'c':1}) == Vec({'a','b','c'}, {'a':0,'c':1,'b':4})) #F
print(Vec({'a','b','c'}, {'a':0,'c':1,'b':4}) == Vec({'a','b','c'}, {'a':0,'c':1})) #F
print(Vec({'a','b'},{'a':1}) == Vec({'a','b'},{'b':1})) #F
print(Vec({'a','b'},{'a':1}) == Vec({'a','b'},{'a':2})) #F

