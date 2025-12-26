import pandas as pd

# Tworzymy proste dane - wyobraź sobie, że to Twój arkusz Excel
dane = {
    'Produkt': ['Chleb', 'Mleko', 'Ser', 'Kawa', 'Herbata'],
    'Cena': [4.50, 3.20, 12.00, 25.00, 8.50],
    'Ilość': [10, 20, 5, 2, 15]
}

# Zamieniamy dane na tzw. DataFrame (podstawowe narzędzie w Pandas)
df = pd.DataFrame(dane)

# 1. Wyświetlamy tabelę
print("--- Cała tabela ---")
print(df)

# 2. Szybkie statystyki (średnia cena, suma produktów)
srednia_cena = df['Cena'].mean()
print(f"\nŚrednia cena produktów: {srednia_cena:.2f} zł")

# 3. Filtrowanie - pokaż tylko drogie produkty (powyżej 10 zł)
drogie_produkty = df[df['Cena'] > 10]
print("\n--- Produkty powyżej 10 zł ---")
print(drogie_produkty)