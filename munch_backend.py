import random

foodWeLike = ['FishAndChips','StirFry','Bangers','Burgers','Pizza','SpanishOmelette','Fajitas']
myMenuList = []
myShoppingList = []

ing_Bangers = ['Banger1','Banger2','Banger3']
ing_Burgers = ['Burger1','Burger2']
ing_Pizza = ['Pizza1','Pizza2','Pizza3']
ing_Fajitas = ['Fajita1','Fajita2']
ing_FishAndChips = ['Fish','Chips']
ing_StirFry = ['Stir','Fry']
ing_SpanishOmelette = ['Spanish','Omelettes']

def chooseDishes(answer):
    while len(myMenuList) < answer:
        dish = random.choice(foodWeLike)
        if dish not in myMenuList:
            myMenuList.append(dish)

    return myMenuList



def buildShoppingList():
    if 'Burgers' in myMenuList:
        for i in range(len(ing_Burgers)):
            myShoppingList.append(ing_Burgers[i])
    if 'Pizza' in myMenuList:
        for i in range(len(ing_Pizza)):
            myShoppingList.append(ing_Pizza[i])
    if 'Bangers' in myMenuList:
        for i in range(len(ing_Bangers)):
            myShoppingList.append(ing_Bangers[i])
    if 'Fajitas' in myMenuList:
        for i in range(len(ing_Fajitas)):
            myShoppingList.append(ing_Fajitas[i])
    if 'FishAndChips' in myMenuList:
        for i in range(len(ing_FishAndChips)):
            myShoppingList.append(ing_FishAndChips[i])
    if 'StirFry' in myMenuList:
        for i in range(len(ing_StirFry)):
            myShoppingList.append(ing_StirFry[i])
    if 'SpanishOmelette' in myMenuList:
        for i in range(len(ing_SpanishOmelette)):
            myShoppingList.append(ing_SpanishOmelette[i])

    def listShoppingList():
        for item in myShoppingList:
            print(item)




        