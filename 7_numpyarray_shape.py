#shape of an array-the shape of an array in the number of elements in each dimension

#now we will try to get the shape of any array
import numpy as np
shared=np.array([[1,2,4,5],[4,5,6,7]])
print(shared.shape)

#(2,4)which means the array is 2 dimension and 4 elements in each dimension
print("\n")

#Now we will create a 3-D array using ndmin:

import numpy as np
shared=np.array([1,2,3,4,5],ndmin=3)
print(shared.shape)

print("\n")

#Now we will create a 4-D array using ndmin:

import numpy as np
shared=np.array([1,2,3,4,5],ndmin=4)
print(shared.shape)

print("\n")
#Now we will create a 5-D array using ndmin:

import numpy as np
shared=np.array([1,2,3,4,5],ndmin=5)
print(shared.shape)

