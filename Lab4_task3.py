# Завдання 3
# Створіть клас для підрахунку максимуму з чотирьох
# аргументів, мінімуму з чотирьох аргументів, середнє
# арифметичне із чотирьох аргументів, факторіалу аргументу. Реалізуйте функціональність у вигляді статичних
# методів.
class MathOperations:
    calculations_count = 0
    @staticmethod
    def find_max(a, b, c, d):
        MathOperations.calculations_count += 1
        return max(a, b, c, d)

    @staticmethod
    def find_min(a, b, c, d):
        MathOperations.calculations_count += 1
        return min(a, b, c, d)

    @staticmethod
    def calculate_average(a, b, c, d):
        MathOperations.calculations_count += 1
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        MathOperations.calculations_count += 1
        if n == 0:
            return 1
        else:
            return n * MathOperations.factorial(n-1)

    @staticmethod
    def get_calculations_count():
        return MathOperations.calculations_count


print("Максимум серед (1, 2, 3, 4):", MathOperations.find_max(1, 2, 3, 4))
print("Мінімум серед (1, 2, 3, 4):", MathOperations.find_min(1, 2, 3, 4))
print("Середнє арифметичне (1, 2, 3, 4):", MathOperations.calculate_average(1, 2, 3, 4))
print("Факторіал 5:", MathOperations.factorial(90))
print("Загальна кількість підрахунків:", MathOperations.get_calculations_count())
