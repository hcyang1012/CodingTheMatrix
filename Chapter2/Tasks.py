# Task 2.4.1
from plotting import plot
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j ,3.25+1j}
plot(S,4)
# End of Task 2.4.3


# Task 2.4.3
from plotting import plot
plot({1+2j+z for z in S},4)
# End of Task 2.4.3


# Task 2.4.10
from image import *
from plotting import plot

data = file2image('img01.png')
data = color2gray(data)
pts = [[x+y*1j for x,pixel in enumerate(row) if pixel < 120] for y, row in enumerate(reversed(data))]
pts1 = sum(pts,[])
plot(pts1,200,1)
# End of Task 2.4.3
