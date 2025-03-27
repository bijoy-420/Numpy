# def my_func(fname):#parameter
#     print("my name is "+ fname)
# my_func("sabbir")#argument
# my_func("bijoy")

# def add(a,b):
#     print(a+b)
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# add(a,b)

#defualt parameter

# def func(country= " Norway"):
#     return "I am from"+ country
# x=func("sweden")
# print(x)

# def func(x):
#     return 5*x
# x=func(4)
# print(x)
# print(func(3))

# print("sabbir", end="\n")
# print("Hossain")

#lamda function

# x=lambda a,b,c:a+b+c
# print(x(5,4,3))

#map function
def func(a):
    return len(a)
x=map(func,['apple',"Banana","Litchi"])
print(list(x))
