import math

class Basics:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")


class Circle(Basics):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        circle_sqm = round(math.pi * (circle.radius ** 2), 2)
        print(f"Circles area based on radius {circle.radius}cm is: {circle_sqm}cm")
        super().describe()
        print(" ")


class Square(Basics):
    def __init__(self,color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        square_sqm = round(square.width ** 2, 2)
        print(f"Squares area based on width {square.width}cm is: {square_sqm}cm")
        super().describe()
        print(" ")

class Triangle(Basics):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        triangle_sqm = round((triangle.width * triangle.height) / 2, 2)
        print(f"Triangles area based on width {triangle.width}cm and height {triangle.height}cm is: {triangle_sqm}cm")
        super().describe()
        print(" ")



circle = Circle("red",True, 5)
square = Square("blue",False, 13.251)
triangle = Triangle("green",False,4.5, 4.75)

square.describe()
triangle.describe()
circle.describe()