#slicing array-slicing in python means taking elements from one given index to another index

#[start:end] or [start:end:step]

#now we will slice an elenemt from 1 to 5:
import numpy as np
shared=np.array([1,2,3,4,5,6,7,8,8,10])
print(shared[1:5])
print(shared[1:])
print(shared[:4])

#Negative indexing support
print(shared[-1:])
print(shared[:-1])

#step- you will use step value to determine the step of the slicing

import numpy as np
shared=np.array([1,2,3,4,5,6,7,8,9,10])
print(shared[1:9])
print(shared[1:9:2])

#now return every other number from the entire array
print(shared[::2])



#Now we will slicing 2-D array,print 6,7,8
import numpy as np
y=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(y[1,0:4])
print(y[0,2:5])

#Another example ,print 3,8

import numpy as np
y=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(y[0:2,2])#y[select row,index which element is select]


