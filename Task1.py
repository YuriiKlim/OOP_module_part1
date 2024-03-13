# Завдання 1
# Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
# дату народження, контактний телефон, місто, країну,
# домашню адресу. Реалізуйте методи класу для введення-виведення даних та інших операцій.
import datetime
import re
class Person:
    def __init__(self, full_name="", date_of_birth="", phone="", city="", country="", address=""):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def input_data(self):
        while True:
            try:
                self.full_name = input("Введіть ПІБ: ")
                if self.full_name.isalpha():
                    break
                else:raise ValueError
            except ValueError:
                print("Неправильне значення")
        self.input_date_of_birth()
        self.input_phone()
        while True:
            try:
                self.city = input("Введіть місто: ")
                if self.city.isalpha():
                    break
                else:raise ValueError
            except ValueError:
                print("Неправильне значення")
        while True:
            try:
                self.country = input("Введіть країну: ")
                if self.country.isalpha():
                    break
                else:raise ValueError
            except ValueError:
                print("Неправильне значення")
        self.address = input("Введіть домашню адресу: ")

    def input_date_of_birth(self):
        while True:
            date_input = input("Введіть дату народження (дд.мм.рррр): ")
            try:
                self.date_of_birth = datetime.datetime.strptime(date_input, "%d.%m.%Y").date()
                break
            except ValueError:
                print("Невірний формат дати. Спробуйте ще раз.")

    def input_phone(self):
        phone_pattern = r"^\+\d+$"
        while True:
            phone_input = input("Введіть контактний телефон у форматі '+12345678': ")
            if re.match(phone_pattern, phone_input):
                self.phone = phone_input
                break
            else:
                print("Невірний формат телефонного номера. Спробуйте ще раз.")

    def display_data(self):
        print("\nДанні про людину")
        print(f"ПІБ: {self.full_name}")
        print(f"Дата народження: {self.date_of_birth}")
        print(f"Контактний телефон: {self.phone}")
        print(f"Місто: {self.city}")
        print(f"Країна: {self.country}")
        print(f"Домашня адреса: {self.address}")

person = Person()
person.input_data()
person.display_data()



