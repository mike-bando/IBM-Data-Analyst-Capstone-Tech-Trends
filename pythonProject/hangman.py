# HangMan
import random
import time
from hangman_wordslist import words


choice = random.choice(words)

#dict of key:()

hangman_art = {0: ("     ",
                   "     ",
                   "     "),
               1: ("  o  ",
                   "     ",
                   "     "),
               2: ("  o  ",
                   "  |  ",
                   "     "),
               3: ("  o  ",
                   " /|  ",
                   "     "),
               4: ("  o  ",
                   " /|\\ ",
                   "     "),
               5: ("  o  ",
                   " /|\\ ",
                   " /   "),
               6: ("  o  ",
                   " /|\\ ",
                   " / \\ ")}


def display_man(wrong_guesses):
    print("*******************")
    for line in hangman_art[wrong_guesses]:
        wrong_guesses += 1
        print(line)
    print("*******************")
def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = list(answer)
    hint = ["_" for x in hint]
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    print("HangMan!")

    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed.")

        guessed_letters.add(guess)
        # print(guessed_letters)
        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        else:
            wrong_guesses +=1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            time.sleep(1)
            print("*******************")
            print("You won!")
            print(f"The correct answer was: {answer}")
            print(f"Amount of wrong guesses: {wrong_guesses}")
            is_running = False
        if wrong_guesses >= len(hangman_art) -1:
            time.sleep(1)
            display_man(6)
            print(f"You have lost. The amount of wrong guesses: {wrong_guesses}")
            print(f"The correct answer was: {answer}")

            break


if __name__ == "__main__":
    main()



# for line in hangman_art[5]:
#     print(line)