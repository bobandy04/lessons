# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
# (using input), compare them, print out a message
# of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:–
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
user1 = []
user2 = ""
while True:
    user1 = input("User1, choose Rock, Paper, Scissors ").lower()
    user2 = input("User2, choose Rock, Paper, Scissors ").lower()

    if user1 == "exit" or user2 == "exit":
        print("One of the users exited the game")
        break

    elif (user1 == "rock" and user2 == "scissors" or user1 == "scissors" and
          user2 == "paper" or user1 == "paper" and user2 == "rock"):
        print("User one wins")

    elif (user2 == "rock" and user1 == "scissors" or user2 == "scissors" and
          user1 == "paper" or user2 == "paper" and user1 == "rock"):
        print("User two wins")

    elif (user1 != "rock" or user1 != "paper" or user1 != "scissors" or
          user2 != "rock" or user2 != "paper" or user2 != "scissors"):
        print("Invalid expression ented")

    elif user1 == user2:
        print("You picked the same thing")

    cont = input("do you want to continue? ").lower()
    if cont == "no":
        print("Thanks for playing!")
        break
