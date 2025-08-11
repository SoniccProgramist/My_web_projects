from abc import ABC, abstractmethod
class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    def get_ingredients(self):
        pass

class Esspresso(Coffee):
    def get_cost(self):
        return 20
    def get_ingredients(self):
        return "coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.decorated_coffee = coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()

class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return super().get_cost() + 10

    def get_ingredients(self):
        return super().get_ingredients() + ", milk"

class SugarDecorator(CoffeeDecorator):
    def get_cost(self):
        return super().get_cost() + 2
    def get_ingredients(self):
        return super().get_ingredients() + ", sugar"

my_coffee = Esspresso()
print(f"My coffee with: cost: {my_coffee.get_cost()}, with ingredients: {my_coffee.get_ingredients()}")

my_coffee = MilkDecorator(my_coffee)
print(f"[After MilkDecorator]My coffee with: cost: {my_coffee.get_cost()}, with ingredients: {my_coffee.get_ingredients()}")

for _ in range(2):
    my_coffee = SugarDecorator(my_coffee)

print(f"[After SugarDecorator twice]My coffee with: cost: {my_coffee.get_cost()}, with ingredients: {my_coffee.get_ingredients()}")
