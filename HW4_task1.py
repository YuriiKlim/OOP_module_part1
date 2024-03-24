# Завдання 1
# До вже реалізованого класу «Дріб» додайте статичний метод, який при виклику повертає кількість створених об’єктів
# класу «Дріб».
class Fraction:
    _object_count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        Fraction._object_count += 1
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        Fraction._object_count += 1
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        Fraction._object_count += 1
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        Fraction._object_count += 1
        return Fraction(new_numerator, new_denominator)

    def simplify(self):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        common_factor = gcd(self.numerator, self.denominator)
        self.numerator //= common_factor
        self.denominator //= common_factor
        Fraction._object_count += 1
        return self

    @staticmethod
    def get_object_count():
        return Fraction._object_count


frac1 = Fraction(3, 4)
frac2 = Fraction(1, 2)

print(f"Додавання: {frac1 + frac2}")
print(f"Віднімання: {frac1 - frac2}")
print(f"Множення: {frac1 * frac2}")
print(f"Ділення: {frac1 / frac2}")

result = frac1 + frac2
print(f"Спрощення: {result.simplify()}")
print(f"Створено об'єктів класу 'Дріб': {Fraction.get_object_count()}")