# Завдання 2
# Реалізуйте клас "Кошик для покупок" з можливістю
# додавання товарів та підрахунку загальної вартості.
# Застосуйте інкапсуляцію для забезпечення правильності
# обробки даних.
class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, name, price):
        """Додає товар у кошик."""
        if isinstance(name, str) and isinstance(price, (int, float)) and price > 0:
            self.__items.append({"name": name, "price": price})
        else:
            print("Некоректні дані товару.")

    def get_total_price(self):
        """Підраховує загальну вартість товарів у кошику."""
        return sum(item["price"] for item in self.__items)

    def display_items(self):
        """Виводить список товарів у кошику та загальну вартість."""
        if not self.__items:
            print("Кошик порожній.")
            return
        print("Товари у кошику:")
        for item in self.__items:
            print(f"- {item['name']}: {item['price']} грн")
        print(f"Загальна вартість: {self.get_total_price()} грн")

cart = ShoppingCart()
cart.add_item("Книга", 300)
cart.add_item("Ручка", 15)
cart.add_item("Зошит", 20)

cart.display_items()
