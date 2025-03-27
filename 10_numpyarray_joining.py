#Array joining -here for this we will pass concatenate()

import numpy as np
shared=np.array([1,2,3,4])
shared1=np.array([5,6,7,8])
n=np.concatenate((shared,shared1))
print(n)


#joining of 2-d arrays along with rows(axis=1)

import numpy as np
x=np.array([[1,2,3,4],[4,5,5,6]])
y=np.array([[3,4,5,6],[5,6,7,8]])
shared=np.concatenate((x,y),axis=1)
print(shared)


#joining array using stack function-

import numpy as np
shared=np.array([1,2,3,4])
shared1=np.array([5,6,7,8])
n=np.stack((shared,shared1),axis=1)
print(n)

#Stacking along with rows:hstack()
import numpy as np
shared=np.array([1,2,3,4])
shared1=np.array([5,6,7,8])
n=np.hstack((shared,shared1))
print(n)

#stacking along with column:vstack()
import numpy as np
shared=np.array([1,2,3,4])
shared1=np.array([5,6,7,8])
n=np.vstack((shared,shared1))
print(n)

#stacking aling with depth:dstack()
import numpy as np
shared=np.array([1,2,3,4])
shared1=np.array([5,6,7,8])
n=np.dstack((shared,shared1))
print(n)