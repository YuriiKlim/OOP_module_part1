# Завдання 2
#  Реалізуйте клас «Стадіон». Збережіть у класі: назву
# стадіону, дату відкриття, країну, місто, місткість. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій. До вже реалізованого класу «Стадіон» додайте
# необхідні перевантажені методи та оператори.
import datetime

class Stadium:
    def __init__(self, name="", opening_date=None, country="", city="", capacity=0):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введіть назву стадіону: ")
        opening_date_str = input("Введіть дату відкриття (дд.мм.рррр): ")
        self.opening_date = datetime.datetime.strptime(opening_date_str, "%d.%m.%Y").date()
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість: "))

    def display_data(self):
        print(f"\nІнформація про стадіон '{self.name}':")
        print(f"Дата відкриття: {self.opening_date.strftime('%d.%m.%Y')}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity}")

    def __str__(self):
        return f"{self.name} в {self.city}, {self.country}. Відкрито: {self.opening_date.strftime('%d.%m.%Y')}, Місткість: {self.capacity}"

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __ne__(self, other):
        return self.capacity != other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

stadium1 = Stadium()
stadium2 = Stadium()

stadium1.input_data()
stadium1.display_data()
print(stadium1)

stadium2.input_data()
stadium2.display_data()
print(stadium2)

if stadium1 > stadium2:
    print(f"{stadium1.name} має більшу місткість, ніж {stadium2.name}")
else:
    print(f"{stadium2.name} має більшу місткість, ніж {stadium1.name}")
