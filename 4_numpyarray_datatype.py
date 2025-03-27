# #data types in python :string,integer,float,bollean,complex
# data type in numpy
# i for integer
# f for float
# u for unsinged integer
# c for complex
# m for timedelta
# M for datatime 
# o for object
# s for string
# U for unicode string
# v for memory

#checking the data type in numpy arrays-integr type

import numpy as np
x=np.array([1,3,4,5,6,7])
print(x.dtype)

#checking the data type in numpy arrays-string type

import numpy as np
x=np.array(['apple','litchi','banana','mango'])
print(x.dtype)


#checking the data type in numpy arrays-float type

import numpy as np
x=np.array([1.3,3.4,4.6,5.1,6.5,7.6])
print(x.dtype)


#Create an array with a defined data types:

x=np.array([1.3,3.4,4.6,5.1,6.5,7.6],dtype="S")
print(x)
print(x.dtype)

#converting data type on existing array-astype()
import numpy as np
x=np.array([1.3,3.4,4.6,5.1,6.5,7.6])
y=x.astype('i')
print(y)

#converting data type from int to boolean
import numpy as np
x=np.array([1,0,3])
y=x.astype(bool)
print(y)