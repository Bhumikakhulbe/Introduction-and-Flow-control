import random
print("This is a 'NUMBER GUESSING GAME'.\nA secret number will be generated between 0 to 100.\nYou have 6 attempts to guess that number.\nALL THE BEST!")
x=random.randint(0,100)  #This function is used to generate a random number between the given range
for i in range(6):
    y=int(input("\nEnter your guess: "))
    if(y>100 or y<0):
        print("The entered number is out of the given range")
    elif (x<y):
        print("Try again!\nThe secret number is smaller than this number.")
    elif (x>y):
        print("Try again!\nThe secret number is larger than this number.")
    else:
        print("congratulations!\nYou guessed the correct number.")
        break
        
print("\nThe game is over.\nThankyou for playing this game!")
