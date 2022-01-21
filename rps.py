import random # Imports some random functions

YourChoice = input("rock, paper, scissors: ")
# Asks the user (You) the choice
rps = ["rock ", "paper", "scissors"]
# This list contains all the game elements (Rock, paper, scissor)
computerChoice = random.choice(rps)
# It makes computer pick a random choice for a "fair" game

print (f"\nYou chose {YourChoice}, computer chose {computerChoice}\n")
# This print code tells you, what you and computer picked when you start playing and pick your choice

if YourChoice == computerChoice: # If you and computer picked the same choice
    print(f"Both you and computer chose {YourChoice}. It's a tie, deal with it") 

elif YourChoice == "rock":
    if computerChoice == "paper":
        print("You really suck at this. Kill yourself mate")
        # If you pick rock and computer paper (You lose)
    else:
        print("Woah, you suck but still you won. Congrats mate")
        # Else you win (If computer picks scissors)
        # There is no rock defined in this because the first if code already declare it as a tie
elif YourChoice == "paper":
    if computerChoice == "rock":
        print("Woah, you suck but still you won. Congrats mate")
        # If you pick paper and computer rock (You win)
    else:
        print("You really suck at this. Kill yourself mate")
        # Else you lose (If computer picks scissors)
        # There is no paper defined in this because the first if code already declare it as a tie
elif YourChoice == "scissors":
    if computerChoice == "rock":
        print("You really suck at this. Kill yourself mate")
        # If you pick scissors and computer picks rock (You lose)
    else:
        print("Woah, you suck but still you won. Congrats mate")
        # Else you win (Computer picks paper)
        # There is no scissors defined in this because the first if code already declare it as a tie


