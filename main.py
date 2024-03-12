# Завдання 2
#  Створіть клас Circle з атрибутом radius та методом
# area, який поверне площу кола з вказаним радіусом.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

circle = Circle(5)
print(f"Площа кола з радіусом {circle.radius} одиниць становить {circle.area()} квадратних одиниць.")


