#Array indexing is the same as accessing an array element start with 0,second 1

import numpy as np
shared=np.array([1,2,4,5,6,7,8])
print(shared[0])

#we can get the third and fourth elements from adding them

import numpy as np
shared=np.array([1,2,3,4,5,6])
print(shared[4]+shared[5])

#Accessing 2-D arrays.it is like as rows and column
import numpy as np
shared=np.array([[12,3,4,54],[3,4,5,6]])
print("Second element first row",shared[1,3])


#Acceessing 3-d array.same as 2-d array

import numpy as np
shared=np.array([[[12,3,4,54],[3,4,5,6]],[[12,3,4,54],[3,4,5,6]]])
print(shared[0,1,2])

