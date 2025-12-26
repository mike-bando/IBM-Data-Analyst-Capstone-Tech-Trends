foods = []
prices = []
total = 0
x=0
srednia_kwota = 0
najwyzsza_kwota = 0
najnizsza_kwota = 0


while True:
    food = input('enter a food to buy (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'enter the price of {food}: $'))
        foods.append(food)
        prices.append(price)


print('')
print('///your cart///')
# print(foods)
# print(prices)

for food, price in zip(foods, prices):
    print(f'{food} = ${price}')
print('\n\n')
srednia_kwota = round(sum(prices)/len(prices),2)
print(f'srednia kwota produktu: ${srednia_kwota}')

najdrozszy_produkt, najwyzsza_kwota = max(zip(foods, prices), key = lambda cena: cena[1])
print(f'najdrozszy produkt: {najdrozszy_produkt}, ktory kosztuje ${najwyzsza_kwota}')

najnizsza_kwota = min(prices)
print(f'najtanszy produkt: ${najnizsza_kwota}')
