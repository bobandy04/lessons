# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
rand = random.randint(1, 9)
guess = []
att = 0
while guess != rand:
    guess = input("Guess a number or type exit ")
    if guess == "exit":
        break
    att = att + 1
    if int(guess) > rand:
        print("too high")
    elif int(guess) < rand:
        print("too low")
    else:
        print("You got it, it only took you " + str(att) + " attempts")
        break
