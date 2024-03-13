# Завдання 3
# Створіть клас «Країна». Збережіть у класі: назву країни,
# назву континенту, кількість жителів країни, телефонний
# код країни, назву столиці, назву міст країни. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій.
class Country:
    def __init__(self, name="", continent="", population=0, phone_code="", capital="", cities=None):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities if cities is not None else []

    def input_data(self):
        while True:
            try:
                self.name = input("Введіть назву країни: ")
                if self.name.isalpha():
                    break
                else: raise ValueError
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.continent = input("Введіть назву континенту: ")
                if self.continent.isalpha():
                    break
                else: raise ValueError
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.population = int(input("Введіть кількість жителів країни: "))
                break
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.phone_code = int(input("Введіть телефонний код країни: "))
                break
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.capital = input("Введіть назву столиці: ")
                if self.capital.isalpha():
                    break
                else: raise ValueError
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                cities_input = input("Введіть назви міст через пробіл: ").lower()
                self.cities = cities_input.split()
                break
            except ValueError:
                print("Неправильне значення")


    def display_data(self):
        print("\nІнформація про країну:")
        print(f"Назва країни: {self.name}")
        print(f"Континент: {self.continent}")
        print(f"Кількість жителів: {self.population}")
        print(f"Телефонний код: {self.phone_code}")
        print(f"Столиця: {self.capital}")
        print("Міста:", ", ".join(self.cities))

    def update_info(self):
        while True:
            print("\nЯку інформацію ви хочете змінити?")
            choice = input(
                "1. Назву країни\n2. Назву континенту\n3. Кількість жителів\n4. Телефонний код\n5. Столицю\n6. Міста\nenter - вихід\nВибір: ")
            if choice == '1':
                while True:
                    try:
                        self.name = input("Введіть нову назву країни: ")
                        if self.name.isalpha():
                            break
                        else: raise ValueError
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '2':
                while True:
                    try:
                        self.continent = input("Введіть нову назву континенту: ")
                        if self.continent.isalpha():
                            break
                        else: raise ValueError
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '3':
                while True:
                    try:
                        self.population = int(input("Введіть нову кількість жителів у країні: "))
                        break
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '4':
                while True:
                    try:
                        self.phone_code = int(input("Введіть новий телефонний код країни: "))
                        break
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '5':
                while True:
                    try:
                        self.capital = input("Введіть нову назву столиці: ")
                        if self.capital.isalpha():
                            break
                        else: raise ValueError
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '6':
                self.edit_cities()
            elif choice == '':
                break
            else:
                print("Невідома опція.")
            country.display_data()

    def edit_cities(self):
        action = input("Ви хочете додати місто чи видалити? (1 - додати, 2 - видалити): ")
        if action == "1":
            while True:
                new_city = input("Введіть назву міста для додавання: ").lower()
                if new_city.isalpha():
                    self.cities.append(new_city)
                    print(f"Місто {new_city} було додано.")
                    break
                else:
                    print("Неправильне значення. Назва міста повинна містити лише букви.")
        elif action == "2":
            while True:
                del_city = input("Введіть назву міста для видалення: ").lower()
                if del_city.isalpha():
                    if del_city in self.cities:
                        self.cities.remove(del_city)
                        print(f"Місто {del_city} було видалено.")
                        break
                    else:
                        print("Такого міста немає у списку.")
                else:
                    print("Неправильне значення. Назва міста повинна містити лише букви.")
        else:
            print("Невідома дія.")


country = Country()
country.input_data()
country.display_data()
country.update_info()