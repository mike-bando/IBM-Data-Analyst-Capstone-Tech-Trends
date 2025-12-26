import curses
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the Speed Typing Test", curses.color_pair(1))
    stdscr.addstr(1, 0, "\nPress any key to continue.", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getch()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    with open("text.txt", "r") as file:
        target_text = file.read()
    current_text = []
    start_time = time.time()
    stdscr.nodelay(True)  # Nie blokuj na czekanie na klawisz

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        try:
            key = stdscr.getkey()
        except:
            continue

        if key == "\x1b":  # Klawisz ESC (ASCII 27)
            break
        if key in (str(curses.KEY_BACKSPACE), "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

        if len(current_text) == len(target_text):
            break

    # Obliczenie poprawnych znaków
    correct_chars = sum(1 for i in range(len(current_text)) if current_text[i] == target_text[i])

    # Wyliczenie finalnego WPM na podstawie całkowitego czasu
    total_time = time.time() - start_time
    final_wpm = round((len(current_text) / (total_time / 60)) / 5)

    stdscr.nodelay(False)  # Wróć do blokowania, czekając na naciśnięcie klawisza
    stdscr.clear()
    stdscr.addstr(0, 0, f"Twój wynik: {final_wpm} WPM")
    stdscr.addstr(1, 0, f"Poprawne znaki: {correct_chars}/{len(target_text)}")
    stdscr.addstr(2, 0, "Naciśnij ESC, aby zakończyć.")
    stdscr.refresh()

    while stdscr.getch() != 27:  # Czekaj na ESC
        pass

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

curses.wrapper(main)