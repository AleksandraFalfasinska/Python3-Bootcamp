import random
print("Welcome to rock, paper, scissors!")

while(True):

    player_wins = 0
    computer_wins = 0
    winner_score = input("How many times you want to play?\n")
    winner_score = int(winner_score)

    while player_wins < winner_score and computer_wins < winner_score:
        print(f"Player score: {player_wins} Computer score: {computer_wins}")
        print("...rock...")
        print("...paper...")
        print("...scissors...")
        print("...If you want to quit press 'q'...")


        player_input = input("Enter your choice: ").lower()
        if player_input == "quit" or player_input == "q":
            break
        computer_move = None
        rand_numb = random.randint(0, 2)

        '''if rand_numb==0:
        print("rock")
        elif rand_numb==1:
        print("paper")
        else:
        print("scissors")'''
        if rand_numb == 0:
            computer_move = "rock"
        elif rand_numb == 1:
            computer_move = "paper"
        else:
            computer_move = "scissors"

        print(f"Computer plays {computer_move}")

        if player_input == computer_move:
            print("It's a tie!")
        elif player_input == "rock":
            if computer_move == "scissors":
                print("Player won")
                player_wins += 1
            else:
                print("Computer won")
                computer_wins += 1
        elif player_input == "scissors":
            if computer_move == "paper":
                print("Player won")
                player_wins += 1
            else:
                print("Computer won")
                computer_wins += 1
        elif player_input == "paper":
            if computer_move == "rock":
                print("Player won")
                player_wins += 1
            else:
                print("Computer won")
                computer_wins += 1

        else:
            print("Enter valid value")


    print(f"Player score: {player_wins} Computer score: {computer_wins}")
    if player_input == "q":
        break

    if player_wins == winner_score:
        print("Congratulations! You won!\n")\

    elif player_wins == computer_wins:
        print("It's a tie!")
    else:
        print("Oh no :( Computer won...")

    print("Do you want play again?")
    
    while(True):
        player_input = input()
        if player_input == "n" or player_input == "y":
            break
        else:
            print("Press 'y' or 'n'")

    if player_input == "n":
        break

