import time





def show_balance(balance):
    print(" ")
    print(f"Your current balance is ${balance:.2f}.")
    print(" ")
def deposit(balance):
    print(" ")
    money_in = float(input("How much money would you like to deposit: "))
    print(f"You have deposited ${money_in}.")
    if money_in < 0:
        print(" ")
        print("That's not the valid amount")
        print(" ")
        return 0
    else:
        return money_in
def withdraw(balance):
    money_out = float(input("How much money would you like to withdraw: "))
    if money_out > balance:
        print(" ")
        print("Your account balance is lower than requested amount to withdraw.")
        print(" ")
        return 0
    elif money_out < 0:
        print(" ")
        print("The amount must be greater than 0.")
        print(" ")
        return 0
    else:
        print(f"You have withdrawn ${money_out}.")
        print(" ")
        return money_out
    

def main():    
    balance = 0
    is_running = True

    while is_running:
        print(" ")
        print("Bank Software:")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit(balance)
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            print("Thank you for using our Services. Goodbye.")
            time.sleep(1)
            break
        else:
            print(" ")
            print("That's not the correct option, try once again by choosing options 1-4.")


if __name__ == "__main__":
    main()
