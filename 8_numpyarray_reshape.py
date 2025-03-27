#Reshaping -means that changing the shape of an array ,like adding or removing the elements

#Reshaping from 1-D to 2-D

import numpy as np
y=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x=y.reshape(4,3)
print(x)

#(4,3) means that 4 is the number of array and 3 is the elemets of each array

print("reshape 1-d to 3-d array \n")

#Reshaping 1-D to 3-D

import numpy as np
y=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x=y.reshape(2,3,2)
print(x)

#converting multidimensional to 1-D array is called flattening

import numpy as np
shared=np.array([[1,2,3,4,5],[3,4,5,6,7]])
x=shared.reshape(-1)
print(x)


