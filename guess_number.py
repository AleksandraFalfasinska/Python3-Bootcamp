import random


player=None


random_number=random.randint(1, 10)

while player != random_number: # I can set while as True, then I have to add 'break' at the end of code (after last print). Moreover the variable 'player' doesn't have to be initialized.
	print("Pick a number between 1 and 10") #first thing which will happen if 'while' equal True
	player=int(input())
	if player>random_number:
		print("You are too high")
	elif player<random_number:
		print("You are too low")
	else:
		print("You won!")
		play_again=input("Do you want keep playing? (y/n):\n" )
		if play_again=="y":
			random_number=random.randint(1, 10)
			player=None
		else:
			print("Thank you for playing")
			


