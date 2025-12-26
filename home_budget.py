"""Home Budget Organiser
1. Wprowadzenie miesiecznego budzetu - Uzytkownik wprowadza calkowity budzet miesieczny (np 5000 zl), 
   kwota ta bedzie wykorzystywana jako punkt odniesienia do porownania z wydatkami.
2. Dodawanie wydatkow - Uzytkownik moze dodawac wydatki do zdefiniowanych kategorii (np. jedzenie, czynsz, transport, inne).
3. Wyswietlanie podsumowania - program wyswietla sume wydatkow w kazdej kategorii. Wyswietla rowniez calkowita sume wydatkow
   oraz roznice miedzy budzetem a wydatkami.
4. Analiza przekroczenia budzetu - jezeli uzytkownik przekroczy budzet, program wyswietla ostrzezenie i kwote przekroczenia.
5. Zakonczenie programu - zapisanie wynikow do pliku tekstowego.
"""

"""Przykładowy scenariusz działania
1.	Użytkownik uruchamia program.
2.	Wprowadza swój budżet (np. 5000 zł).
3.	Dodaje wydatki:
    •	Jedzenie: 500 zł
    •	Transport: 300 zł
    •	Rozrywka: 200 zł
4.	Wyświetla podsumowanie:
    •	Jedzenie: 500 zł
    •	Transport: 300 zł
    •	Rozrywka: 200 zł
    •	Suma wydatków: 1000 zł
    •	Pozostały budżet: 4000 zł
5.	Dodaje więcej wydatków i przekracza budżet.
6.	Program ostrzega, że budżet został przekroczony o 200 zł.
7.	Zamyka program i zapisuje podsumowanie do pliku."""
# import
import os, sys, time



# funkcje
def totalBudget():
    # funkcja pobiera kwote budzetu od uzytkownika
    budget = int(input("Podaj budzet miesieczny: "))
    print(f'Budzet miesieczny wynosi: {budget} zl.')
    return budget

def spendings(budget):
    categories = {
    1: {'name': 'Jedzenie', 'amount': 0},
    2: {'name': 'Transport', 'amount': 0},
    3: {'name': 'Czynsz', 'amount': 0},
    4: {'name': 'Pozostale', 'amount': 0}
}
    leftoverMoney = 0
    spendingAmount = 0
    time.sleep(1)
    while True:
        print('')
        print('Podstawowe kategorie wydatkow:')
        print('1. Jedzenie')
        print('2. Transport')
        print('3. Czynsz')
        print('4. Pozostale')
        print('')
    
        chosenCategory = int(input('Wybierz kategorie wydatku:(1-4, lub 0 aby pokazac podsumowanie): '))
        if chosenCategory in categories:
            category_name = categories[chosenCategory]
            print(f'Wybrano kategorię "{categories[chosenCategory]['name']}"')
            amountToAdd = int(input(f"Ile miesięcznie wydajesz na {categories[chosenCategory]['name']}?: "))
            spendingAmount += amountToAdd
            categories[chosenCategory]['amount'] += amountToAdd
        elif chosenCategory == 0:
            print('')
            print('')
            print('*** Podsumowanie: ***')
            time.sleep(1)
            print(f'Laczne wydatki miesieczne wynosza {spendingAmount} zl.')
            for cat in categories.values():
                print(f"{cat['name']}: {cat['amount']} zł")
            
            time.sleep(0.5)
            leftoverMoney = budget - spendingAmount
            print(f'Pozostanie {leftoverMoney} zl.')
            print('')
            break
        else:
            print('Wybrano zla kategorie.')
            break 

    

# glowny program
print('')
print('Witamy w Organizerze Budzetu domowego!')
spendingCategories = ['Jedzenie','Transport','Czynsz','Pozostale']
budget = totalBudget()
time.sleep(0.5)
spendings(budget)
