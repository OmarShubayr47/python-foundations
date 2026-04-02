import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors)")
    options = ["rock", "paper","scissors"]
    computer_choice = random.choice(options)
    choices ={"player" : player_choice, "computer" : computer_choice}
    return choices
def check_win(player,computer):
    print (f"You chose {player}, Computer chose {computer}.")
    if player == computer:
         print ("It's a tie!")
    elif player == "rock" and computer == "scissors":
         print("Player wins!")
    elif player == "paper" and computer == "rock":
         print("Player wins!")
    elif player == "scissors" and computer == "paper":
         print("Player wins!")
    else:
         print("Computer wins!")


check_win("rock","paper")