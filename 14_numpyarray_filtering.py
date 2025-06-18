#Filtering array-Getting some elements out of an existing array and creating a new array is called filtering 
#A boolean index list is a list of boolean corossponding to indexes in the array.(True and  False)
#create an array from the element on index 0 to 2:

import numpy as np
shared=np.array([1,2,3,4,5,6,7,8,9,10])
x=[]
for i in shared:
    if i>5:
        x.append(i)

    
print(x)