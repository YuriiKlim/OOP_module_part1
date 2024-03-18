# Завдання 4
# Реалізуйте клас «Годинник». Збережіть у класі:
# назву моделі годинника, виробника годинника, рік
# випуску, ціну годинника, тип годинника (наручний,
# настінний і т. д.). Реалізуйте конструктор та методи
# класу для введення-виведення даних, а також для
# інших операцій. Використовуйте механізм
# перевантаження методів.
import re
class Watch:
    def __init__(self, model_name="", manufacturer="", release_year=0, price=0.0, watch_type=""):
        self.model_name = model_name
        self.manufacturer = manufacturer
        self.release_year = release_year
        self.price = price
        self.watch_type = watch_type

    def input_text(self, prompt, pattern=r"^[A-Za-zА-Яа-яЁё\s'-]+$"):
        while True:
            data = input(prompt)
            if re.match(pattern, data):
                return data
            else:
                print("Неправильне значення. Спробуйте ще раз.")

    def input_number(self, prompt, type_1=int):
        while True:
            try:
                return type_1(input(prompt))
            except ValueError:
                print("Неправильне значення. Спробуйте ще раз.")
    def input_number_float(self, prompt, type_=float):
        while True:
            try:
                return type_(input(prompt))
            except ValueError:
                print("Неправильне значення. Спробуйте ще раз.")

    def input_data(self):
        self.model_name = self.input_text("Введіть назву моделі годинника: ")
        self.manufacturer = self.input_text("Введіть виробника годинника: ")
        self.release_year = self.input_number("Введіть рік випуску: ")
        self.price = self.input_number_float("Введіть ціну годинника: ")
        self.watch_type = self.input_text("Введіть тип годинника (наручний, настінний тощо): ")

    def display_data(self):
        print("\nІнформація про годинник:")
        print(f"Модель: {self.model_name}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Рік випуску: {self.release_year}")
        print(f"Ціна: {self.price} грн")
        print(f"Тип: {self.watch_type}")

    def __eq__(self, other):
        return (self.model_name == other.model_name) and (self.manufacturer == other.manufacturer) and (self.watch_type == other.watch_type)

    def __lt__(self, other):
        return self.release_year < other.release_year

    def __gt__(self, other):
        return self.price > other.price

# Використання класу
watch1 = Watch()
watch2 = Watch()

watch1.input_data()
watch1.display_data()

watch2.input_data()
watch2.display_data()

if watch1.model_name == watch2.model_name:
    print("Годинники однакові.")
else:
    print("Годинники різні.")
if watch1.manufacturer == watch2.manufacturer:
    print("Один виробник.")
else:
    print("Різні виробники.")

if watch1.release_year < watch2.release_year:
    print(f"Годинник {watch1.model_name} старіший за {watch2.model_name}.")
else:
    print(f"Годинник {watch2.model_name} старіший за {watch1.model_name}.")

if watch1.price > watch2.price:
    print(f"Годинник {watch1.model_name} дорожчий за {watch2.model_name}.")
else:
    print(f"Годинник {watch2.model_name} дорожчий за {watch1.model_name}.")
if watch1.watch_type == watch2.watch_type:
    print("Типи годинників однакові.")
else:
    print("Типи годинників різні.")
