# # Programowanie obiektowe

# class User:
#     age = 0
#     def print_age(self, additional_message):
#         print(additional_message,'--',self.name,'wiek:',self.age)

#     def __init__(self, age, name):
#         # print("Inicjalizator, ktory wywoluje sie zawsze podczas konstrukcji obiektu")
#         self.age = age
#         self.name = name
#         self.AgeInFuture = age + 1



# user1 = User(30, "Arek")
# user2 = User(24, "Mirek")

# user1.print_age('')
# user2.print_age('')

# print(f"Wiek uzytkownika {user1.name} za rok: {user1.AgeInFuture}")

#rakieta leca w gore na randomowa wysokosc

import random 
from math import sqrt

class Rocket:
    """
    Cokolwiek blablabla
    """
    def __init__(self,speed=1, altitude=0, x=0):    
        self.altitude = random.randint(1, 500)
        self.speed = speed
        self.x = 0

    def __str__(self):
        return 'Rakieta aktualnie jest na wysokosci: '+str(self.altitude)
    
    def moveUp(self):
        self.altitude += self.speed

    
    
class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket() for _ in range(amountOfRockets)]
        for _ in range(10):
            rocketIndexToMove = random.randint(0, len(self.rockets)-1)
            self.rockets[rocketIndexToMove].__str__()

        # for rocket in self.rockets:
        #     print(rocket)

    def __getitem__(self,key):
        return self.rockets[key]
    

    def __setitem__(self,key,value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(rocket1, rocket2):
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2      

        return int(sqrt(ab+bc))
    
