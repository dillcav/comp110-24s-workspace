"""Number guessing game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while not correct: # same as correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    elif guess > SECRET:
        print("Too high! Try again!")
    else:
        print("Too low! Try again!")