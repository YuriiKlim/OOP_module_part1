# Завдання 2
# Створіть клас для підрахунку площі геометричних
# фігур. Клас має надавати функціональність підрахунку
# площі трикутника за різними формулами, площі прямокутника, площі квадрата, площі ромба. Методи класу для
# підрахунку площі реалізуйте за допомогою статичних
# методів. Також клас має розрахувати кількість підрахунків площі та повернути це значення статичним методом
import math

class AreaCalculator:
    calculations_count = 0

    @staticmethod
    def calculate_triangle_area_by_base_and_height(base, height):
        AreaCalculator.calculations_count += 1
        return 0.5 * base * height

    @staticmethod
    def calculate_triangle_area_by_sides(a, b, c):
        s = (a + b + c) / 2
        AreaCalculator.calculations_count += 1
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    @staticmethod
    def calculate_rectangle_area(length, width):
        AreaCalculator.calculations_count += 1
        return length * width

    @staticmethod
    def calculate_square_area(side):
        AreaCalculator.calculations_count += 1
        return side ** 2

    @staticmethod
    def calculate_rhombus_area(diagonal1, diagonal2):
        AreaCalculator.calculations_count += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_calculations_count():
        return AreaCalculator.calculations_count


print("Площа трикутника:", AreaCalculator.calculate_triangle_area_by_base_and_height(10, 5))
print("Площа трикутника:", AreaCalculator.calculate_triangle_area_by_sides(3, 4, 5))
print("Площа прямокутника:", AreaCalculator.calculate_rectangle_area(10, 20))
print("Площа квадрата:", AreaCalculator.calculate_square_area(5))
print("Площа ромба:", AreaCalculator.calculate_rhombus_area(10, 8))
print("Загальна кількість підрахунків площі:", AreaCalculator.get_calculations_count())