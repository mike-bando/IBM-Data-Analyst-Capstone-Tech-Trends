import random


options = ('rock','paper','scissors')

gaming = True


while gaming:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice(rock, paper, scissors): ")

        print(f'Player: {player}')
        print(f'Computer: {computer}')

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "rock" and computer == "paper":
            print("Computer wins!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        elif player == "scissors" and computer == "rock":
            print("Computer wins!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "paper" and computer == "scissors":
            print("Computer wins!")

    if not input("Play again? (y/n): ").lower() =='y':
        gaming = False


print("Thanks for playing!")