import os
import csv

# --- KONFIGURACJA ---
# Zmień ścieżkę na tę, w której znajdują się Twoje pliki wideo
folder_sciezka = r"/Users/michalbando/Downloads/MTA_RAW_REVIEW" 
nazwa_pliku_csv = "lista_plikow1.csv"
# --- KONIEC KONFIGURACJI ---

# Definicja nagłówków dla pliku CSV
naglowki = ['timestamp_unix', 'identyfikator', 'nazwa_kamery', 'pelna_nazwa_pliku']

# Lista do przechowywania danych o plikach
dane_plikow = []

# Pobranie listy plików z folderu
try:
    pliki = os.listdir(folder_sciezka)
except FileNotFoundError:
    print(f"BŁĄD: Folder '{folder_sciezka}' nie został znaleziony. Sprawdź ścieżkę.")
    exit()

print(f"Znaleziono {len(pliki)} plików. Rozpoczynam przetwarzanie...")

# Pętla przez wszystkie pliki w folderze
for nazwa_pliku in pliki:
    if nazwa_pliku.endswith('.mkv'):
        try:
            czesci = nazwa_pliku.split('_')
            timestamp_str = czesci[0]
            identyfikator_str = czesci[1]
            nazwa_kamery_str = "_".join(czesci[2:]).replace('.mkv', '')

            # Dodanie danych do listy
            dane_plikow.append([timestamp_str, identyfikator_str, nazwa_kamery_str, nazwa_pliku])

        except IndexError:
            print(f"Pominięto plik o nieprawidłowym formacie nazwy: {nazwa_pliku}")

# Zapis danych do pliku CSV
try:
    with open(nazwa_pliku_csv, mode='w', newline='', encoding='utf-8') as plik:
        writer = csv.writer(plik)
        writer.writerow(naglowki)  # Zapis nagłówków
        writer.writerows(dane_plikow) # Zapis wszystkich danych
    print(f"\nGotowe! Dane zostały zapisane do pliku '{nazwa_pliku_csv}'.")
except IOError:
    print(f"BŁĄD: Nie można zapisać pliku '{nazwa_pliku_csv}'. Sprawdź uprawnienia.")