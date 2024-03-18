# Завдання 2
# До вже реалізованого класу «Місто» додайте конструктор та необхідні перевантажені методи.
import re
class City:
    def __init__(self, name="", region="", country="", population=0, postal_code=0, phone_code=0):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_string_data(self, prompt, pattern=r"^[A-Za-zА-Яа-яЁё\s-]+$"):
        while True:
            value = input(prompt)
            if re.match(pattern, value):
                return value
            else:
                print("Неправильне значення. Будь ласка, введіть коректні дані.")

    def input_numeric_data(self, prompt, data_type=int):
        while True:
            try:
                value = data_type(input(prompt))
                return value
            except ValueError:
                print("Неправильне значення. Будь ласка, введіть число.")

    def input_data(self):
        self.name = self.input_string_data("Введіть назву міста: ")
        self.region = self.input_string_data("Введіть назву регіону: ")
        self.country = self.input_string_data("Введіть назву країни: ")
        self.population = self.input_numeric_data("Введіть кількість жителів у місті: ")
        self.postal_code = self.input_numeric_data("Введіть поштовий індекс міста: ")
        self.phone_code = self.input_numeric_data("Введіть телефонний код міста: ")

    def display_data(self):
        print("\nІнформація про місто:")
        print(f"Назва міста: {self.name}")
        print(f"Назва регіону: {self.region}")
        print(f"Назва країни: {self.country}")
        print(f"Кількість жителів: {self.population}")
        print(f"Поштовий індекс: {self.postal_code}")
        print(f"Телефонний код: {self.phone_code}")


    # def update_info(self):
    #     options = {
    #         '1': ("назву міста", "name", True),
    #         '2': ("назву регіону", "region", True),
    #         '3': ("назву країни", "country", True),
    #         '4': ("кількість жителів у місті", "population", True),
    #         '5': ("поштовий індекс міста", "postal_code", True),
    #         '6': ("телефонний код міста", "phone_code", True)
    #     }
    #     while True:
    #         print("\nЯку інформацію ви хочете змінити?")
    #         for key, (desc, _, _) in options.items():
    #             print(f"{key}. {desc}")
    #         choice = input("Введіть номер опції або натисніть Enter для виходу: ")
    #         if choice in options:
    #             desc, attr, *allow_space = options[choice]
    #             if attr in ["population", "postal_code", "phone_code"]:
    #                 setattr(self, attr, self.input_numeric_data(f"Введіть нову {desc}: "))
    #             else:
    #                 setattr(self, attr, self.input_string_data(f"Введіть нову {desc}: ", *allow_space))
    #             self.display_data()
    #         elif choice == '':
    #             break
    #         else:
    #             print("Невідома опція.")

    def __gt__(self, other):
        return self.population > other.population

    def __add__(self, other):
        return self.population + other.population

    def __sub__(self, other):
        return abs(self.population - other.population)


city1 = City()
city2 = City()
city1.input_data()
city2.input_data()
city1.display_data()
city2.display_data()
#city.update_info()
max_city = max(city1.population, city2.population)
min_city = min(city1.population, city2.population)
if city1 > city2:
    print(f"У {city1.name} більше населення, ніж у {city2.name}.")
else:
    print(f"У {city2.name} більше населення, ніж у {city1.name}.")

print(f"Сумарне населення {city1.name} і {city2.name} становить: {city1 + city2}")

print(f"Різниця в населенні між {city1.name} і {city2.name} становить: {max_city - min_city}")

city = City()


