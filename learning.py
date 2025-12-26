import munch_backend, random, sys
from time import sleep

"""
Munch
Let's roll!
"""

answer = 0


print("Hi, I'm Munch! I'll help you to plan your dinner menu!")
answer = int(input('How many days would you like to plan for? (1-7): '))


if answer == 0:
    print('0 is not an option, try once again!')
    answer = int(input('How many days would you like to plan for? '))
    print("")    
    print(f"Okay! I'm going to plan {answer} day(s) of meals!")
    print("")
elif answer == 1:
    print("Okay! I'm going to plan 1 day meal for you!")
    print("")

elif answer in (2,3,4,5,6,7):
    print("")    
    print(f"Okay! I'm going to plan {answer} days of meals!")
    print("")

else:
    print('Your answer is not correct.')
    sleep(0.5)
    sys.exit()
    
munch_backend.chooseDishes(answer)

sleep(1)
print('Okay, here is your Meal Menu!:')
for meal in munch_backend.myMenuList:
    print(meal)
    sleep(0.3)
print("")
favouriteMeal = random.choice(munch_backend.myMenuList)
print(f'Out of all of these dishes, my favourite has to be... {favouriteMeal}')
print("")

sleep(1)
answer1 = input('Would you like to the shopping list for these meals? (yes/no): ')
if answer1 == 'yes':
    munch_backend.buildShoppingList()
    print("")
    sleep(1)
    print(f"Here's your shopping list:")
    for item in munch_backend.myShoppingList:
        print(item)
        sleep(0.1)
elif answer1 == 'no':
    print("No problem, have a great week!")
else:
    print("Your answer is not correct, I'm done.")