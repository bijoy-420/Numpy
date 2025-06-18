#Permutation -refers to an arrangement of elements like [3,2,1] is permutation of [1,2,3] and vice-versa

#the numpy random module provides 2 method :shuffle() and permutation()

#now we will randomly shuffle elements for the below array
#shuffle() make change to the origianl array

from numpy import random
import numpy as np
shared=np.array([1,2,3,4,5,6])
random.shuffle(shared)
print(shared)

#now we will generate a permutation of elements for the below array:
#the permutation() method leaves the original array unchanged

from numpy import random
import numpy as np
shared=np.array([1,2,3,4,5,6])
x=random.permutation(shared)

print(x)

