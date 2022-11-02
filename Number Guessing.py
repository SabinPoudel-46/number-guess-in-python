#Number Guessing Game in Python
import random as r #importing random function
win_number=r.randint(1,10) #using randint function to generate number in between 1 and 10
count=1
guess_number=int(input("Enter a number between 1 and 10: "))
while 1:
    if guess_number>10:
        print("Invalid input")
        break
    elif guess_number==win_number:
        if count==1:
            print(f"You have Guessed number in {count}st attempt")
            break
        elif count==2:
            print(f"You have Guessed number in {count}nd attempt")
            break
        elif count==3:
            print(f"You have Guessed number in {count}rd attempt")
            break
        else:
            print(f"You have Guessed number in {count}th attempt")
            break
    elif guess_number>win_number:
        print("You Guessed a Bigger Number")
        guess_number=int(input("Enter a number between 1 and 10: "))
        count+=1
    else:
        print("You Guessed a smaller number")
        guess_number=int(input("Enter a number between 1 and 10: "))
        count+=1

