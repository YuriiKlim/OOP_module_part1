# Завдання 1
# Створіть систему управління замовленнями
# готелю. Кожне замовлення має містити інформацію
# про клієнта, тип кімнати, кількість днів проживання та
# вартість. Реалізуйте методи для додавання замовлення,
# зміни типу кімнати та кількості днів, а також
# видалення замовлення. Використайте інкапсуляцію для
# захисту вартості від неправильних змін.
class HotelOrder:
    room_options = {
        "1": ("Стандарт", (500, 1000)),
        "2": ("Бізнес", (1000, 1500)),
        "3": ("Люкс", (2000, 3000)),
        "4": ("Президентський", (3000, 5000))
    }
    def __init__(self, client_name, room_type, days, cost_per_day):
        self.client_name = client_name
        self.room_type = room_type
        self.days = days
        self.__cost_per_day = cost_per_day
        self.__total_cost = self.__calculate_total_cost()

    def __calculate_total_cost(self):
        """Приватний метод для розрахунку загальної вартості."""
        return self.__cost_per_day * self.days

    def input_number(self, prompt, type_=int):
        while True:
            try:
                return type_(input(prompt))
            except ValueError:
                print("Неправильне значення. Спробуйте ще раз.")
    def update_room_type(self):
        """Оновлення типу кімнати та вартості за день через вибір користувача з діапазоном цін."""

        print("Виберіть новий тип кімнати:")
        for key, (type, _) in self.room_options.items():
            print(f"{key} - {type}")

        choice = input("Ваш вибір: ")
        if choice in self.room_options:
            self.room_type, price_range = self.room_options[choice]
            while True:
                try:
                    new_price = float(input(f"Введіть нову ціну за день для типу '{self.room_type}' "
                                            f"у діапазоні {price_range[0]}-{price_range[1]}: "))
                    if price_range[0] <= new_price <= price_range[1]:
                        self.__cost_per_day = new_price
                        self.__total_cost = self.__calculate_total_cost()
                        print(f"Тип кімнати оновлено на {self.room_type} з новою ціною {self.__cost_per_day:g} за день.")
                        break
                    else:
                        print("Ціна повинна бути в межах вказаного діапазону.")
                except ValueError:
                    print("Некоректне значення ціни.")
        else:
            print("Невірний вибір. Тип кімнати не оновлено.")

    def update_info(self):
        options = {
            '1': self.update_room_type,
            '2': self.update_cost_per_day,
            '3': self.update_days,
        }
        while True:
            print("\nЯку інформацію ви хочете змінити?")
            descriptions = {
                '1': "Змінити тип кімнати",
                '2': "Змінити вартість за день",
                '3': "Змінити кількість днів проживання",
            }
            for key, desc in descriptions.items():
                print(f"{key}. {desc}")
            choice = input("Введіть номер опції або натисніть Enter для виходу: ")
            if choice in options:
                if choice == '2':
                    while True:
                        if self.room_type == "Стандарт":
                            new_cost = self.input_number(f"Введіть нову ціну за день у діапазоні "
                                                         f"{self.room_options["1"][1][0]}-{self.room_options["1"][1][1]}: ")
                            if self.room_options["1"][1][0] <= new_cost <= self.room_options["1"][1][1]:
                                break
                            else:
                                print("Ціна повинна бути в межах вказаного діапазону.")
                        elif self.room_type == "Бізнес":
                            new_cost = self.input_number(f"Введіть нову ціну за день у діапазоні "
                                                         f"{self.room_options["2"][1][0]}-{self.room_options["2"][1][1]}: ")
                            if self.room_options["2"][1][0] <= new_cost <= self.room_options["2"][1][1]:
                                break
                            else:
                                print("Ціна повинна бути в межах вказаного діапазону.")
                        elif self.room_type == "Люкс":
                            new_cost = self.input_number(f"Введіть нову ціну за день у діапазоні "
                                                         f"{self.room_options["3"][1][0]}-{self.room_options["3"][1][1]}: ")
                            if self.room_options["3"][1][0] <= new_cost <= self.room_options["3"][1][1]:
                                break
                            else:
                                print("Ціна повинна бути в межах вказаного діапазону.")
                        elif self.room_type == "Президентський":
                            new_cost = self.input_number(f"Введіть нову ціну за день у діапазоні "
                                                         f"{self.room_options["4"][1][0]}-{self.room_options["4"][1][1]}: ")
                            if self.room_options["4"][1][0] <= new_cost <= self.room_options["4"][1][1]:
                                break
                            else:
                                print("Ціна повинна бути в межах вказаного діапазону.")
                    self.__cost_per_day = new_cost
                elif choice == '3':
                    new_days = self.input_number("Введіть нову кількість днів: ")
                    self.update_days(new_days)
                else:
                    options[choice]()
                self.__total_cost = self.__calculate_total_cost()
                self.get_order_info()
            elif choice == '':
                return
                break
            else:
                print("Невідома опція.")
    def update_cost_per_day(self, new_cost):
        """Оновлення ціни за день, хотів у цьому методі прописати весь код для зміни, але все ломалось"""
        self.__cost_per_day = new_cost
        self.__total_cost = self.__calculate_total_cost()
        print("Вартість за день оновлено.")
    def update_days(self, new_days):
        """Оновлення кількості днів проживання."""
        self.days = new_days
        self.__total_cost = self.__calculate_total_cost()

    def get_order_info(self):
        """Виводить інформацію про замовлення."""
        print(f"\nКлієнт: {self.client_name}\nТип кімнати: {self.room_type}\nДні: {self.days}\nВартість за день: {self.__cost_per_day:g}\nЗагальна вартість: {self.__total_cost:g}")

order1 = HotelOrder("Юрій Клім", "Стандарт", 5, 900)
order1.get_order_info()

order1.update_info()

