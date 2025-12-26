import time
import random

def wyswietl_zasady():
    """Wyświetla zasady gry."""
    print("--- ZASADY GRY W 21 ---")
    print("Gracze na zmianę podają od 1 do 3 kolejnych liczb.")
    print("Celem jest zmuszenie przeciwnika (komputera) do powiedzenia liczby 21.")
    print("Osoba, która powie '21', przegrywa.")
    print("-------------------------\n")

def pobierz_ruch_gracza(aktualna_liczba):
    """Pobiera i waliduje ruch gracza."""
    while True:
        try:
            # Pytamy, ile liczb gracz chce podać
            ile_liczb = int(input("Ile liczb chcesz podać (1-3)? > "))

            # Sprawdzamy, czy gracz podał poprawną ilość
            if ile_liczb < 1 or ile_liczb > 3:
                print("Błędna wartość. Możesz podać od 1 do 3 liczb.")
                continue

            # Pytamy o kolejne liczby i sprawdzamy ich poprawność
            podane_liczby = []
            for i in range(ile_liczb):
                oczekiwana_liczba = aktualna_liczba + i + 1
                liczba = int(input(f"Podaj liczbę {oczekiwana_liczba}: > "))
                
                # Sprawdzamy, czy gracz podał kolejną, oczekiwaną liczbę
                if liczba != oczekiwana_liczba:
                    print(f"Błędna liczba! Oczekiwano {oczekiwana_liczba}, a podano {liczba}.")
                    print("Przegrywasz z powodu pomyłki.")
                    return -1 # Sygnał przegranej przez błąd
                
                podane_liczby.append(liczba)
            
            print(f"Podałeś liczby: {podane_liczby}")
            return podane_liczby[-1] # Zwracamy ostatnią podaną liczbę

        except ValueError:
            print("To nie jest liczba! Podaj poprawną wartość.")

def wykonaj_ruch_komputera(aktualna_liczba):
    """Wykonuje ruch komputera zgodnie ze zwycięską strategią."""
    print("\n--- Tura Komputera ---")
    
    # Celem komputera jest zawsze dojście do wielokrotności liczby 4 (4, 8, 12, 16, 20)
    cel = ((aktualna_liczba // 4) + 1) * 4
    
    # Jeśli cel jest poza zasięgiem (np. ostatnia liczba to 18, a cel to 20),
    # komputer musi podać tyle liczb, by dojść do 20.
    if cel > 20:
        cel = 20
        
    ile_liczb = cel - aktualna_liczba

    # Jeśli komputer nie może dojść do wielokrotności 4 (bo gracz go zablokował),
    # wykonuje losowy ruch (1-3), aby gra toczyła się dalej.
    if ile_liczb == 0 or ile_liczb > 3:
        ile_liczb = random.randint(1, 3)

    podane_liczby = []
    for i in range(ile_liczb):
        podane_liczby.append(aktualna_liczba + i + 1)
    
    print(f"Komputer podaje liczby: {podane_liczby}")
    time.sleep(1) # Pauza dla realizmu
    return podane_liczby[-1] # Zwracamy ostatnią podaną liczbę

def start_gry():
    """Główna funkcja rozpoczynająca grę."""
    aktualna_liczba = 0
    tura_gracza = False # Domyślnie komputer zaczyna, chyba że gracz wybierze inaczej

    # Pytamy gracza, kto ma zacząć
    while True:
        wybor = input("Kto zaczyna? Wpisz 'ja' lub 'komputer': > ").lower()
        if wybor == 'ja':
            tura_gracza = True
            break
        elif wybor == 'komputer':
            tura_gracza = False
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

    # Główna pętla gry
    while aktualna_liczba < 21:
        if tura_gracza:
            print(f"\n--- Twoja Tura (ostatnia liczba to {aktualna_liczba}) ---")
            aktualna_liczba = pobierz_ruch_gracza(aktualna_liczba)

            # Sprawdzamy, czy gracz przegrał (podał 21 lub popełnił błąd)
            if aktualna_liczba >= 21:
                print("\nPodałeś liczbę 21! Przegrywasz.")
                return # Koniec gry
        else:
            aktualna_liczba = wykonaj_ruch_komputera(aktualna_liczba)
            
            # Sprawdzamy, czy komputer przegrał (co oznacza wygraną gracza)
            if aktualna_liczba >= 21:
                print("\nKomputer musiał podać 21! WYGRYWASZ!")
                return # Koniec gry

        # Zmiana tury
        tura_gracza = not tura_gracza

# --- Uruchomienie programu ---
wyswietl_zasady()

while True:
    start_gry()
    
    ponownie = input("\nCzy chcesz zagrać jeszcze raz? (tak/nie): > ").lower()
    if ponownie != 'tak':
        print("Dzięki za grę!")
        break
