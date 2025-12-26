# import requests
# from bs4 import BeautifulSoup

# # 1. Pobieramy stronę (tak jak wcześniej)
# url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# headers = {'User-Agent': 'Mozilla/5.0...'} # Twój User-Agent
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')

# # --- TERAZ ZACZYNA SIĘ ANALIZA ---

# # A. Wyciągnij TYTUŁ strony (to co w tagu <h1>)
# tytul = soup.find('h1').text
# print(f"Tytuł artykułu: {tytul}")

# # B. Wyciągnij WSZYSTKIE nagłówki sekcji (tagi <h2>)
# # .find_all zwraca listę, więc możemy po niej pętlić
# print("\n--- Spis treści (Sekcje) ---")
# sekcje = soup.find_all('h2')
# for sekcja in sekcje:
#     # .text usuwa znaczniki html, .strip() usuwa spacje
#     print("- " + sekcja.text.strip())

# # C. Wyciągnij pierwszy prawdziwy akapit tekstu
# # Wikipedia jest trudna, bo ma dużo śmieci na początku, ale spróbujmy:
# print("\n--- Fragment tekstu ---")
# paragrafy = soup.find_all('p')
# # Zazwyczaj 2. lub 3. paragraf to ten właściwy tekst
# if len(paragrafy) > 2:
#     print(paragrafy[2].text)


# import pandas as pd

# # Pandas szuka wszystkich tabel na stronie i zwraca listę DataFrame'ów
# tabele = pd.read_html('https://en.wikipedia.org/wiki/Python_(programming_language)')

# # Bierzesz pierwszą tabelę
# df = tabele[0]
# print(df.head())

# 1. IMPORTY - Narzędzia, których będziemy używać
import requests                 # Kurier (do pobrania strony)
from bs4 import BeautifulSoup   # Bibliotekarz (do czytania HTML)
import pandas as pd             # Analityk (do tabeli i Excela)

# ==========================================
# KROK 1: REQUESTS (Pobieranie paczki)
# ==========================================

# Adres strony z danymi o przejęciach IBM
url = "https://en.wikipedia.org/wiki/List_of_IBM_acquisitions"

# Nasz dowód osobisty (udajemy przeglądarkę)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print("1. Wysyłam kuriera po stronę...")
response = requests.get(url, headers=headers)

# Sprawdzamy czy kurier wrócił cały i zdrowy (Kod 200)
if response.status_code == 200:
    print("   Sukces! Paczka odebrana.")
else:
    print(f"   Błąd! Kod: {response.status_code}")
    exit() # Kończymy program, jeśli nie ma strony

# ==========================================
# KROK 2: PARSER (Rozpakowanie paczki)
# ==========================================

print("2. Rozpakowuję HTML i gotuję zupę (BeautifulSoup)...")
# html.parser układa nam surowy tekst w drzewo obiektów
soup = BeautifulSoup(response.text, 'html.parser')

# ==========================================
# KROK 3: BS4 (Wyciąganie "mięska")
# ==========================================

print("3. Szukam tabeli z danymi...")

# Szukamy tabeli, która ma klasę 'wikitable' (standard na Wikipedii)
# sortable oznacza, że to ta duża tabela z danymi
tabela = soup.find('table', class_='wikitable')

# Przygotowujemy pustą listę na nasze odkrycia
lista_firm = []

# Pobieramy wszystkie WIERSZE z tabeli (tag <tr> - table row)
# Pomijamy pierwszy wiersz ([1:]), bo to nagłówki (Date, Company, itp.)
wiersze = tabela.find_all('tr')[1:]

print(f"   Znalazłem {len(wiersze)} przejętych firm. Przetwarzam...")

for wiersz in wiersze:
    # W każdym wierszu szukamy KOLUMN (tag <td> - table data)
    kolumny = wiersz.find_all('td')
    
    # Zabezpieczenie: czy wiersz na pewno ma kolumny? (czasem są puste)
    if len(kolumny) > 1:
        # --- EKSTRAKCJA DANYCH ---
        # Kolumna 0 to Data, Kolumna 1 to Nazwa Firmy, Kolumna 2 to Branża
        
        data_przejecia = kolumny[0].text.strip()
        nazwa_firmy = kolumny[1].text.strip()
        branza = kolumny[2].text.strip()
        
        # Tworzymy słownik dla jednej firmy
        firma = {
            "Data": data_przejecia,
            "Firma": nazwa_firmy,
            "Branża": branza
        }
        
        # Wrzucamy do worka
        lista_firm.append(firma)

# ==========================================
# KROK 4: PANDAS (Raport końcowy)
# ==========================================

print("4. Tworzę DataFrame (Excel)...")

# Zamieniamy listę słowników na tabelę Pandas
df = pd.DataFrame(lista_firm)

# Opcjonalnie: czyścimy daty lub sortujemy
# (Tutaj tylko wyświetlimy wynik)

print("\n--- WYNIK KOŃCOWY (Pierwsze 5 wierszy) ---")
print(df.head())

# Opcjonalnie: Zapis do pliku
# df.to_csv('ibm_przejecia.csv', index=False)
# print("\nZapisano do pliku ibm_przejecia.csv")