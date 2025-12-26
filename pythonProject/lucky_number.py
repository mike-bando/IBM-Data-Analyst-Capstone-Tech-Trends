import random


low_number = 1
high_number = 100

number = random.randint(low_number, high_number)
guesses = 0
while True:
    choice = input(f'Choose number (between {low_number} and {high_number}): ')
    if choice.isdigit():
        choice = int(choice)
        guesses +=1
        if choice > number and choice < high_number:
            print("the chosen number is higher than the lucky number, try once again")
        elif choice < number and choice > low_number:
            print('the chosen number is lower than the lucky number, try once again')
        elif choice == number:
            print("perfect, you've found the lucky number!")
            
            print(f"you've found the number in {guesses} guesses")
            break
        elif choice > high_number:
            print(f"That number is higher than {high_number}, try once again")
        elif choice < low_number:
            print(f"that number is lower than {low_number}, try again.")
    else:
        print(f"that's an invalid guess. Type the number between {low_number} and {high_number}")
        