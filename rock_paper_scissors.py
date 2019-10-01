# Aaron Fuller
#Rock paper scissors game

#
# Break into pieces
# Welcome screen, with name entry
# Score screen with computer and player, using the name
# Options for game are r, p, s, and q
# Game will loop until q is pressed
# Each loop it will get a random choice from the computer
# A choice from the player, compare the two, and update the score
# When the game is over (q is entered) final score is displayed

# WELCOME PAGE
# Prompt for the player name
# A welcome message

#

# Imports
import random
# Variables
playerScore = 0
computerScore = 0
ties = 0
# Make a list
cChoices = ["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name:")
# Main loop
while True:
# Print Score
	print("Score:")
	print("Computer: " + str(computerScore))
	print(name + ": " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit:")
	computerChoice = random.choice(cChoices)
	print(computerChoice)
	if choice == "q":
		break

	if choice == "r":
		print(name + " Picked Rock")
		if computerChoice == "r": # Tie
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rock")
			computerScore += 1
		else: # s is the only other variable
			print("Computer picked Scissors")
			print("Rock beats Scissors")
			playerScore += 1
	elif choice == "p":
			print(name + " Picked Paper")
			if computerChoice == "r":
				print("Computer picked Rock")
				print("Paper beats Rock")
				playerScore += 1
			elif computerChoice == "p":
				print("Computer picked Paper")
				print("This is a tie")
				ties = ties + 1
			else:
				print("Computer picked Scissors")
				print("Scissors beat Paper")
				computerScore += 1
	elif choice == "s":
		print(name + " Picked Scissors")
		if computerChoice == "p":
			print("Computer picked Papers")
			print("Scissors beats Paper")
			playerScore += 1
		elif computerChoice == "r":
			print("Computer picked Rock")
			print("Rock beats Scissors")
			computerScore += 1
		else:
			print("Computer picked scissors")
			print("This is a tie")
			ties = ties + 1
	else:# Print type something else
		print("Type something else")
