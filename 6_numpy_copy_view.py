#Main differnce between numpy copy and view

#we will make a copy ,it can't change in original array,and display both

import numpy as np 
shared=np. array([1,2,3,4,5])
x=shared.copy()
x[0]=9
print(shared)
print(x)

print("\n")
#Now we will discuss about the view,it can change the original array and display both

import numpy as np 
shared=np. array([1,2,3,4,5])
y=shared.view()

y[0]=10
print(shared)
print(y)
