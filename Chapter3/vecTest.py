from vec import Vec

newVec = Vec({'A','B','C'},{'A':1.0})
print(newVec['A'])
newVec['B'] = 4.0
print(newVec['B'])
newVec['C'] = 5.0
print(newVec['C'])
newVec['B'] = newVec['C'] = 6.0
print(newVec['B'])
print(newVec['C'])
