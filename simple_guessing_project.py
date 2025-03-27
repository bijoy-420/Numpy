import random
number=random.randint(1,100)
while(True):
    guess=int(input("Enter your guessing number:"))
    if guess<number:
        print("Too Low! Try Again")
    elif guess>number:
        print("High! Try Again")
    else:
        print("Congratulations! you guess the correct Number")
    
        break 
       
