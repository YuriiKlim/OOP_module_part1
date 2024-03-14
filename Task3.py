# Завдання 3
#  До вже реалізованого класу «Автомобіль» додайте
# необхідні перевантажені методи та оператори.
import datetime
class Car:
    def __init__(self, brand="", model="", year=0):
        self.brand = brand
        self.model = model
        self.year = year
    def start_engine(self):
        if self.year > 1980:
            print(f"Двигун {self.brand} {self.model} {self.year} року запущено.")
        else:
            print(f"{self.brand} {self.model} {self.year} року не завівся =(")

    def __str__(self):
        return f"Автомобіль: {self.brand} {self.model}, Рік випуску: {self.year}"

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.year < other.year

car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Toyota", "Camry", 2022)
car3 = Car("Ford", "Mustang", 1968)

print(f"{car1} і {car2} однакові:", car1 == car2)
print(f"{car1} і {car3} різні:", car1 != car3)

if car1 < car3:
    print(f"{car1.model} {car1.year} року випуску молодший за {car3.model} {car3.year} року.")
else:
    print(f"{car3.model} {car3.year} року випуску старший за {car1.model} {car1.year} року.")

car1.start_engine()
car3.start_engine()


