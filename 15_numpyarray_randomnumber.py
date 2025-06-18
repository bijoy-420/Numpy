#Random meaning-something that can not be predicted logically

#now we will generate a random number

#import numpy as np
from numpy import random
shared=random.randint(100)
print(shared)

#you can also generate float() via rand()
shared=random.rand()
print(shared)

#you can also generate random array

#we wwill generate a 1-D array containing 5 random number from 0 to 100:

import numpy as np
shared=np.random.randint(100,size=5)
print(shared)

#we wwill generate a 2-D array  with 3 rows each rows containing 5 random number from 0 to 100:

import numpy as np
shared=np.random.randint(100,size=(3,5))
print(shared)

#we wwill generate a 1-D array containing 5 random  float number from 0 to 100:

import numpy as np
shared=np.random.rand(5)
print(shared)


#you can alos generate random numbers from an array
#choice()

shared=random.choice([2,3,4,5,7,8,9,1])
print(shared)

#you can alos generate random numbers from 2-D array
#choice()

shared=random.choice([2,3,4,5,7,8,9,1],size=(3,5))
print(shared)

