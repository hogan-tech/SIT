# Author: Hogan Lin
# Date: Sept 23th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Use while loop to guess the x, y value, and set chance with 3 times. use if elif else to setting the different condition


import random

guessesRemaining = 3

# Set random x and y coordinates for the particle (or you can choose specific values)
particleX = random.randint(1, 10)
particleY = random.randint(1, 10)

# While loop that continues as long as the user has guesses remaining
while guessesRemaining > 0:
    # Inform the user of how many guesses are left
    print(
        f"The particle is somewhere in this space! You have {guessesRemaining} chances to guess it.")

    guessX = int(input("What do you think its x coordinate is (1-10)? "))
    guessY = int(input("What do you think its y coordinate is (1-10)? "))

    # Check if the guessed coordinates are within bounds
    if guessX < 1 or guessX > 10 or guessY < 1 or guessY > 10:
        print(f"No good! ({guessX},{guessY}) is outside of the range!")
    # Check if the guessed coordinates are correct
    elif guessX == particleX and guessY == particleY:
        print(f"Good guess! ({guessX},{guessY}) was the position!")
        break  # Exit the loop if the user guessed correctly
    else:
        # Give hints based on the user's guess
        if guessX > particleX:
            print("Bad luck! The particle's x position is less than your x position!")
        elif guessX < particleX:
            print("Bad luck! The particle's x position is greater than your x position!")

        if guessY > particleY:
            print("Bad luck! The particle's y position is less than your y position!")
        elif guessY < particleY:
            print("Bad luck! The particle's y position is greater than your y position!")

    # Decrement the number of guesses remaining
    guessesRemaining -= 1

    # If the user runs out of guesses, end the game
    if guessesRemaining == 0:
        print(
            f"\nOh no! You ran out of chances. ({particleX},{particleY}) was the particle's position!")
