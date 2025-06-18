#Searching array-you can search an array for a certain value and return the indexes that get the match by using where()

import numpy as np
shared=np.array([1,2,3,4,5,4,4])
x=np.where(shared==4)
print(x)

#where() return the index of the searching value

#now we will  find the indexes where the values are even:

shared=np.array([1,2,3,4,5,6,7,8])
x=np.where(shared%2==0)
print(x)

#now we will  find the indexes where the values are odd:

shared=np.array([1,2,3,4,5,6,7,8])
x=np.where(shared%2!=0)
print(x)

#searchsorted()-perform binary search in array.
#we will now find the index where the value 7 should be inserted

shared=np.array([6,7,8,9])
x=np.searchsorted(shared,7)
print(x)

#now we will search from the right side
shared=np.array([6,7,8,9])
x=np.searchsorted(shared,7,side='right')
print(x)

#How to search multiple values:
shared=np.array([6,7,8,9])
x=np.searchsorted(shared,[6,8])
print(x) 


