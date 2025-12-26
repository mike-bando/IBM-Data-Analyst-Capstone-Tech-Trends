from rocket import RocketBoard, Rocket
from random import randint


# board = RocketBoard(5)
# board[0].altitude= 40
# board[0].x = 4


# rocket1 = Rocket(altitude=3,x=4)
# rocket2 = Rocket()
# print(board[0])
# print(board[1])
# print(f'Odleglosc miedzy rakietami: {board.get_distance(board[0],board[1])}')


# print(f'Rakieta 1 na wysokosci: {rocket1.altitude}')
# print(f'Rakieta 2 na wysokosci: {rocket2.altitude}')
# print(f'Odleglosc miedzy rakietami: {RocketBoard.get_distance(rocket1, rocket2)}')

myRocket = Rocket(altitude=3, x=4)
anotherRocket = Rocket(altitude=1, x=30)
x:float = RocketBoard.get_distance(myRocket, anotherRocket)
print(x)
