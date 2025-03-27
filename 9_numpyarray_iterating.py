#iterating array-means that going through the elements one by one or step by step like loop

#iterate the elements of 1-D

import numpy as np
x=np.array([1,2,3,4,5,6,7,6])
for i in x:
    print(i)
    
#iterate 2-D array
shared=np.array([[1,2,3,4],[2,3,4,5]])
for i in shared:
    print(i)
    
#iterate the each elements 

shared=np.array([[1,2,3,4],[2,3,4,5]])
for i in shared:
    for j in i:
        print(j)
        
#iterate 3-D array,iterate each elements


shared=np.array([[[1,2,3,4],[2,3,4,5]],[[1,2,3,4],[2,3,4,5]]])
for i in shared:
    for j in i:
        for z in j:
            print(z)
            
            
#iterating using nditer function
#now we will iterate each elements

import numpy as np
x=np.array([[[1,2,3,4],[2,3,4,5]],[[1,2,3,4],[2,3,4,5]]])
for i in np.nditer(x):
    print(i)
    
print("\n")
    
#Now we will iterate with differnet step size:

shared=np.array([[1,2,3,4],[2,3,4,5]])
for i in np.nditer(shared[:,::2]):
    print(i)
    
