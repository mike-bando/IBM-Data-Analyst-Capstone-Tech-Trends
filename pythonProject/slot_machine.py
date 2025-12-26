# Python Slot Machine
import random, time



def spin_row():
    symbols = ['🍒', '🍋', '🍏', '🔔' ,'⭐️']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
    # return [random.choice(symbols) for _ in range(3)]    

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        elif row[0] == '🍏':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐️':
            return bet * 20
    
    return 0
    


def main():
    balance = 100
    
    print(" ")
    print("Welcome to Python Slot Machine!")
    print("Symbols: ")
    print("🍒 🍋 🍏 🔔 ⭐️")
    print(" ")


    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = int(input("Place your bet amount: $"))
        if bet > balance:
            print(f"You don't have enough money. Your balance is ${balance}")
            continue
        elif bet <= 0:
            print(f"Bet can't be lower or equal to 0.")
            continue
        else:       
            balance -= bet
        play_again = input("Do you want to play again? (Y/N): ").upper()

        if play_again != "Y":
            break
    
        print(" ")
        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        time.sleep(0.5)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round.")
            print(" ")
        balance += payout
    else:
        print("You don't have any funds. Game over.") 
        


if __name__ == "__main__":
    main()



