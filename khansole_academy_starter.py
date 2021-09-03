"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
count=0
while count!=3:
    num1=random.randint(5,60)
    num2=random.randint(10,50)
    total=num1+num2
    print(num1 ,'+',num2)
    ans=int(input("Enter the answer >> "))
    if ans==total:
        count=count+1
        print("You have answered ",count," in a row")
    else:
        print("SORRY... the right answer is ",total)
        count=0
print("You have mastered it !") 