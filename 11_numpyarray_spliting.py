#Spliting arrays in numpy.it is reverse to joining,breaking the array.
#Array Spliting

#split the array in three parts
import numpy as np
shared=np.array([1,2,3,4,5,6,7,8,9])
x=np.array_split(shared,3)
print(x)

#now we will split this array into 4 parts
import numpy as np
shared=np.array([1,2,3,4,5,6,7,8,9])
x=np.array_split(shared,4)
print(x)


#split into arrays with index

import numpy as np
shared=np.array([1,2,3,4,5,6,7,8,9])
x=np.array_split(shared,4)
print(x[0])
print(x[1])
print(x[2])

#spliting the 2-D arrays

import numpy as np
shared=np.array([[1,2,3,4],[6,7,8,9]])
x=np.array_split(shared,2)
print(x)


#spliting the 2-D array into three 2-D array along the rows
import numpy as np
shared=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
x=np.array_split(shared,3,axis=1)
print(x)
  
#Alternating solution is using the hsplit(),opposite hstack()
import numpy as np
shared=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
x=np.hsplit(shared,3)
print(x)
  
  
