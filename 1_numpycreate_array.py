#Now we will create a numpy ndarray object
#the array object in numpy is call nd array
#array()

import numpy as np
x=np.array([1,2,3,4,5])
print(x)
print(type(x))

#we can also pass a list,tuple or any array like object with array().and it will be converted into ndarray
import numpy as np
y=np.array((1,2,3,4,5))
print(y)
print(type(y))
print(y.ndim)

#Dimension in arrays - A dimension in arrays is one level arrays depth(nested arrays)

# 0-d arrays - scalars are the element in an array , each value in an array is a 0-d array

#Now we will create 0_d  Array with a value with 10
import numpy as np
z=np.array(10)
print(z)
print(z.ndim)

#1- d array -an array that has 0-d arrays as its elememts is called uni directional or 1-d
import numpy as np
shared=np.array([1,2,3,4,5])
print(shared)
print(shared.ndim)

#Create a 2-d arrays containing 2 arrays waith certain values
import numpy as np
x=np.array([[1,2,3,4],[3,4,5,2]])
print(x)
print(x.ndim) #ndim attributes used for dimension of arrays

#Now create 3-d arrays with two 2-d arrays.
import numpy as np
y=np.array([[[1,2,3,4],[3,4,5,2]],[[1,2,3,4],[3,4,5,2]]])
print(y)
print(y.ndim)

#create an array with five dimension and verify that its has five dimension

shared=np.array([1,2,3,4,5,6,4],ndmin=5)#ndmin define the deimension
print(shared)
print(shared.ndim)
