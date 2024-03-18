import re

class Country:
    def __init__(self, name="", continent="", population=0, phone_code="", capital="", cities=None):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities if cities is not None else []

    def input_text(self, prompt, pattern=r"^[A-Za-zА-Яа-яЁё\s'-]+$"):
        while True:
            data = input(prompt)
            if re.match(pattern, data):
                return data
            else:
                print("Неправильне значення. Спробуйте ще раз.")

    def input_number(self, prompt, type_=int):
        while True:
            try:
                return type_(input(prompt))
            except ValueError:
                print("Неправильне значення. Спробуйте ще раз.")

    def input_data(self):
        self.name = self.input_text("Введіть назву країни: ")
        self.continent = self.input_text("Введіть назву континенту: ")
        self.population = self.input_number("Введіть кількість жителів країни: ")
        self.phone_code = self.input_number("Введіть телефонний код країни: ")
        self.capital = self.input_text("Введіть назву столиці: ")
        cities_input = self.input_text("Введіть назви міст через пробіл: ")
        self.cities = cities_input.split(' ')

    def display_data(self):
        print("\nІнформація про країну:")
        print(f"Назва країни: {self.name}")
        print(f"Континент: {self.continent}")
        print(f"Кількість жителів: {self.population}")
        print(f"Телефонний код: {self.phone_code}")
        print(f"Столиця: {self.capital}")
        print("Міста:", ", ".join(self.cities))

    # def update_info(self):
    #     options = {
    #         '1': ('назву країни', self.input_text),
    #         '2': ('назву континенту', self.input_text),
    #         '3': ('кількість жителів', self.input_number),
    #         '4': ('телефонний код', self.input_text),
    #         '5': ('назву столиці', self.input_text),
    #         '6': ('редагувати міста', self.edit_cities)
    #     }
    #     while True:
    #         print("\nЯку інформацію ви хочете змінити?")
    #         for key, (desc, _) in options.items():
    #             print(f"{key}. {desc}")
    #         choice = input("Введіть номер опції або натисніть Enter для виходу: ")
    #         if choice in options:
    #             desc, func = options[choice]
    #             if choice != '6':
    #                 setattr(self, desc.split()[1], func(f"Введіть {desc}: "))
    #             else:
    #                 func()
    #             self.display_data()
    #         elif choice == '':
    #             break
    #         else:
    #             print("Невідома опція.")
    #
    # def edit_cities(self):
    #     action = input("Ви хочете додати місто (1) чи видалити (2)?: ")
    #     if action == '1':
    #         new_city = self.input_text("Введіть назву міста для додавання: ")
    #         self.cities.append(new_city)
    #         print(f"Місто {new_city} додано.")
    #     elif action == '2' and self.cities:
    #         del_city = self.input_text("Введіть назву міста для видалення: ")
    #         if del_city in self.cities:
    #             self.cities.remove(del_city)
    #             print(f"Місто {del_city} видалено.")
    #         else:
    #             print("Місто не знайдено.")
    def __gt__(self, other):
        return self.population > other.population
    def __lt__(self, other):
        return self.population < other.population
    def __add__(self, other):
        total_population = self.population + other.population
        return total_population
    def __sub__(self, other):
        difference_population = abs(self.population - other.population)
        return difference_population
    def __eq__(self, other):
        return self.continent == other.continent

country1 = Country()
country2 = Country()
country1.input_data()
country2.input_data()
country1.display_data()
country2.display_data()
#country.update_info()

if country1 > country2:
    print(f"У {country1.name} більше населення, ніж у {country2.name}.")
else:
    print(f"У {country2.name} більше населення, ніж у {country1.name}.")
print(f"Сумарне населення {country1.name} і {country2.name} становить: {country1 + country2} людей")
print(f"Різниця в населенні між {country1.name} і {country2.name} становить: {country1 - country2} людей")
print(f"Чи знаходяться {country1.name} і {country2.name} на одному континенті? {'Так' if country1.continent == country2.continent else 'Ні'}")
