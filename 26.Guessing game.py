from random import randint
"""
import random

#if we use little number
guessNumber = int(input("Enter your guess between 1 to 5"))
randomNumber = random.randint(1,5)

#if we use biggest number
randomNumber = random.random() * 100
"""

guessNumber = int(input("Enter your guess between 1 to 5: "))
randomNumber = randint(1,5)

if guessNumber == randomNumber:
    print("You have won")
else:
    print("You have lost")
    print("Random number was: ",randomNumber)





