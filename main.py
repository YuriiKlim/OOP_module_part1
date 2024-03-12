# Завдання 4
#  Створіть клас Car з атрибутами brand (марка
# автомобіля), model (модель) та year (рік випуску).
# Додайте метод start_engine, який виведе повідомлення
# про те, що двигун запущено.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        if self.year > 1980:
            print(f"Двигун {self.brand} {self.model} {self.year} року запущено.")
        else: print("винь-винь-винь, не завівся =(")

my_car = Car("Toyota", "Camry", 2022)
my_car.start_engine()

