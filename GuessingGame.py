import random

chances = 5
number = random.randint(1,9)
print("Number Guessing Game")
while chances != 0:
    guess = int(input("Enter Your Guess Number: "))
    
    if guess == number:
        print("Congrats You Won!!!")
        break

    if guess > number:
        print("Your a Number Larger than the number")
        
    if guess < number:
        print("Your a Number Smaller than the number")


    chances -=1 

if chances == 0:
    print("Better Luck Next Time")