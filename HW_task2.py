# Завдання 2
# Розробіть систему управління замовленнями таксі.
# Кожне замовлення має містити інформацію про
# клієнта, адресу, тип автомобіля та вартість. Реалізуйте
# методи для додавання нових замовлень, зміни адреси та
# типу автомобіля, а також видалення замовлення.
# Використайте інкапсуляцію для захисту вартості від
# неправильних змін.
class TaxiOrder:
    car_types = {
        "1": "Стандарт",
        "2": "Бізнес",
        "3": "Люкс",
        "4": "Мінівен"
    }

    def __init__(self, client_name, in_address, out_address, car_type, cost):
        self.client_name = client_name
        self.in_address = in_address
        self.out_address = out_address
        self.car_type = car_type
        self.__cost = cost

    def __calculate_total_cost(self):
        return self.__cost

    def update_address(self):
        while True:
            choise = input("Виберіть, яку адресу ви хочете змінити 1 -адреса посадки, 2 - адреса висадки")
            if choise == "1":
                self.in_address = input("Введіть нову адресу посадки: ")
                print(f"Адресу посадки оновлено: {self.in_address}")
                break
            elif choise == "2":
                self.out_address = input("Введіть нову адресу висадки: ")
                print(f"Адресу висадки оновлено: {self.out_address}")
                break
            else: print("Неправильний вибір")

    def update_car_type(self, new_car_type_key):
        if new_car_type_key in self.car_types:
            self.car_type = self.car_types[new_car_type_key]
            print(f"Тип автомобіля замовлення оновлено: {self.car_type}")
        else:
            print("Невідповідний ключ типу автомобіля.")

    def get_order_info(self):
        return f"Замовлення: {self.client_name}, Адреса посадки: {self.in_address}, Адреса висадки: {self.out_address},Тип автомобіля: {self.car_type}, Вартість: {self.__cost}"

class TaxiOrderManagement:
    def __init__(self):
        self.orders = []

    def input_number(self, prompt, type_=float):
        while True:
            try:
                return type_(input(prompt))
            except ValueError:
                print("Неправильне значення. Спробуйте ще раз.")

    def create_order(self):
        client_name = input("Ім'я клієнта: ")
        in_address = input("Адреса посадки: ")
        out_address = input("Адреса висадки: ")
        print("Тип автомобіля:")
        for key, value in TaxiOrder.car_types.items():
            print(f"{key}: {value}")
        car_type_key = input("Виберіть тип автомобіля: ")
        car_type = TaxiOrder.car_types.get(car_type_key, "Стандарт")
        cost = self.input_number("Введіть ціну: ")
        order = TaxiOrder(client_name, in_address, out_address, car_type, cost)
        self.orders.append(order)
        print("Замовлення створено.")

    def list_orders(self):
        if not self.orders:
            print("Замовлення відсутні.")
        else:
            for index, order in enumerate(self.orders, start=1):
                print(f"{index}. {order.get_order_info()}")

    def select_order(self):
        """Вибір замовлення для редагування або видалення."""
        self.list_orders()
        if not self.orders:
            return
        choice = int(input("Виберіть номер замовлення: ")) - 1
        if 0 <= choice < len(self.orders):
            selected_order = self.orders[choice]
            while True:
                print(f"\nВибрано замовлення: {selected_order.client_name}")
                selected_order.get_order_info()
                print("\n1. Редагувати замовлення\n2. Видалити замовлення\nenter - Повернутися до головного меню")
                action = input("Ваш вибір: ")
                if action == "1":
                    self.update_order(choice)
                elif action == "2":
                    self.del_order(choice)
                    break
                elif action == "":
                    break
                else:
                    print("Невідома опція. Спробуйте ще раз.")
        else:
            print("Невірний вибір замовлення.")

    def update_order(self, order_index):
        if 0 <= order_index < len(self.orders):
            order = self.orders[order_index]
            print("Оберіть параметр для оновлення:\n1. Адреса\n2. Тип автомобіля")
            choice = input("Ваш вибір: ")
            if choice == "1":
                order.update_address()
            elif choice == "2":
                print("Тип автомобіля:")
                for key, value in TaxiOrder.car_types.items():
                    print(f"{key}: {value}")
                new_car_type_key = input("Виберіть новий тип автомобіля: ")
                order.update_car_type(new_car_type_key)
            else:
                print("Невідомий вибір.")
        else:
            print("Некоректний індекс замовлення.")

    def del_order(self, order_index):
        if 0 <= order_index < len(self.orders):
            del self.orders[order_index]
            print("Замовлення видалено.")
        else:
            print("Некоректний індекс замовлення.")

def main():
    management = TaxiOrderManagement()
    while True:
        print("\nуправління замовленнями таксі")
        print("1. Створити нове замовлення\n2. Переглянути всі замовлення\nenter - Вийти")
        choice = input("Введіть ваш вибір: ")
        if choice == "1":
            management.create_order()
        elif choice == "2":
            management.select_order()
        elif choice == "":
            print("Вихід з програми.")
            break
        else:
            print("Невідома опція. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
