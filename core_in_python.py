#start pyhton program 

print("Hello world!")

#single line comment denoted by (#)
#and multiline comment denoted by ("""""")




#variables

x=5
y="sabbir"
print(x,y)

#a="awesome"
def myfunc():
   global a
   a="fantastic"
    #print("pyhton is " + a)
    
myfunc()
print("python is "+a)

import random
print(random.randrange(1,10))
#list (constructor list)
thislist=list(("mango","Banana","Litchi","Tomato"))
print(thislist)

#list item access (list allow negative indexing)
print(thislist[-1])
#we can also print range of a list

print(thislist[1:])
#check the item is contain or not
if "apple" not in thislist:
    print("the apple is in the list")
    

#change the list item
thislist[3]="apple"
print(thislist)

#insert item in the list

thislist.insert(3,"carret")
print(thislist)

#add item in the list
thislist.append("orange")
print(thislist)

#add two list in one list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove item in the list
thislist.remove("Banana")
thislist.pop(1)
print(thislist)

#using loop in the list
for x in thislist:
    print(x)
    
#using while loop
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1

#list comprehension
new=[]
for x in thislist:
    if "a" in x:
        new.append(x)
print(new)
new.sort(reverse=True)
print(new)

#copy the list
mylist=list(thislist)
print(mylist)

#join two  list
list3=thislist+mylist
for x in mylist:
    thislist.append(x)
print(thislist)


#tuple is immutable or unchangeable 
"""if we want to change into the tuple at first convert the tuple into list than change the tuple"""
import function
function.add(a, b)