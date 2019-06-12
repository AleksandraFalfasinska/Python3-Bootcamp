import random
print("Welcome to rock, paper, scissors!")
player_wins= 0
computer_wins= 0
winner_score= input("How many times you want to play?\n")
winner_score= int(winner_score)

while player_wins < winner_score and computer_wins < winner_score:
	print(f"Player score: {player_wins} Computer score: {computer_wins}")
	print ("...rock...")
	print ("...paper...")
	print ("...scissors...")

	Player= input("Enter your choice: ").lower()
	if Player == "quit" or Player == "q":
		break
	Computer= None
	rand_numb= random.randint(0, 2)

	'''if rand_numb==0:
	print("rock")
	elif rand_numb==1:
	print("paper")
	else:
	print("scissors")'''
	if rand_numb == 0:
		computer = "rock"
	elif rand_numb == 1:
		computer = "paper"
	else:
		computer = "scissors"								

	print(f"Computer plays {computer}")


	if Player == Computer:
		print("It's a tie!")
	elif Player == "rock":
		if Computer == "scissors":
			print("Player won")
			player_wins += 1
		else:
			print("Computer won")
			computer_wins += 1
	elif Player =="scissors":
		if Computer == "paper":
			print("Player won")
			player_wins += 1
		else:
			print("Computer won")
			computer_wins += 1
	elif Player =="paper":
		if Computer == "rock":
			print("Player won")
			player_wins += 1
		else:
			print("Computer won")
			computer_wins += 1

	else:
		print("Enter valid value")

print(f"Player score: {player_wins} Computer score: {computer_wins}")
			
if player_wins == winner_score:
	print("Congratulations! You won!")
elif player_wins == computer_wins:
	print("It's a tie!")
else:
	print("Oh no :( Computer won...")