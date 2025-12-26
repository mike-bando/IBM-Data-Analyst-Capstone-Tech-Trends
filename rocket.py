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
        self.rockets = [Rocket(random.randint(1,6)) for _ in range(amountOfRockets)]
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
    def get_distance(obj1: Rocket, obj2: Rocket) -> float:
        ab = (obj1.altitude - obj2.altitude) ** 2
        bc = (obj1.x - obj2.x) ** 2      

        return int(sqrt(ab+bc))
    
            
