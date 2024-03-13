# Завдання 2
# Створіть клас «Місто». Збережіть у класі: назву міста,
# назву регіону, назву країни, кількість жителів у місті,
# поштовий індекс міста, телефонний код міста. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій.
class City:
    def __init__(self, name="", region="", country="", population=0, postal_code=0, phone_code=0):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        while True:
            try:
                self.name = input("Введіть назву міста: ")
                if self.name.isalpha():
                    break
                else: raise ValueError
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.region = input("Введіть назву регіону: ")
                if self.region.isalpha():
                    break
                else: raise ValueError
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.country = input("Введіть назву країни: ")
                if self.country.isalpha():
                    break
                else: raise ValueError
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.population = int(input("Введіть кількість жителів у місті: "))
                break
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.postal_code = int(input("Введіть поштовий індекс міста: "))
                break
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.phone_code = int(input("Введіть телефонний код міста: "))
                break
            except ValueError:
                print("Неправильне значення")

    def display_data(self):
        print("\nІнформація про місто:")
        print(f"Назва міста: {self.name}")
        print(f"Назва регіону: {self.region}")
        print(f"Назва країни: {self.country}")
        print(f"Кількість жителів: {self.population}")
        print(f"Поштовий індекс: {self.postal_code}")
        print(f"Телефонний код: {self.phone_code}")

    def update_info(self):
        while True:
            print("\nЯку інформацію ви хочете змінити?")
            choice = input(
                "1. Назву міста\n2. Назву регіону\n3. Назву країни\n4. Кількість жителів\n5. Поштовий індекс\n6. Телефонний код\nenter - вихід\nВибір: ")
            if choice == '1':
                while True:
                    try:
                        self.name = input("Введіть нову назву міста: ")
                        if self.name.isalpha():
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '2':
                while True:
                    try:
                        self.region = input("Введіть нову назву регіону: ")
                        if self.region.isalpha():
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '3':
                while True:
                    try:
                        self.country = input("Введіть нову назву країни: ")
                        if self.country.isalpha():
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '4':
                while True:
                    try:
                        self.population = int(input("Введіть нову кількість жителів у місті: "))
                        break
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '5':
                while True:
                    try:
                        self.postal_code = int(input("Введіть новий поштовий індекс міста: "))
                        break
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '6':
                while True:
                    try:
                        self.phone_code = int(input("Введіть новий телефонний код міста: "))
                        break
                    except ValueError:
                        print("Неправильне значення")
            elif choice == '':
                break
            else:
                print("Невідома опція.")
            city.display_data()


city = City()
city.input_data()
city.display_data()
city.update_info()
city.display_data()

