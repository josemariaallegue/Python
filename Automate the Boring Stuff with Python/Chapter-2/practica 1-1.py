import random
from typing import SupportsRound

i = random.randint(1,20)
guess = 0
contador = 0

print("I am thinking of a number between 1 and 20.")
print("Take a guess")
print(str(i))

while guess != i:

    guess = int(input())
    contador += 1

    if(guess == i):
        print("Good job! You guessed my number in " + str(contador) +" guesses!")
        break
    elif(guess < i):
        print("Your guess is too low.")
    elif(guess > i):
        print("Your guess is too high.")