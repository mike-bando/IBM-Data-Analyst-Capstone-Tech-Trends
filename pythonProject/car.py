class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")

    def describe(self):
        print(f"Your chosen car is {self.model}, year {self.year}, color {self.color}")
        print(f"Is your {self.model} for sale?: {self.for_sale}")