# Завдання 3
# Запрограмуйте клас Money (об’єкт класу оперує однією
# валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої
# частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання
# значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
# зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.
class Money:
    def __init__(self, whole_part, fractional_part):
        self._whole_part = whole_part
        self._fractional_part = fractional_part

    def get_amount(self):
        print(f"{self._whole_part}.{self._fractional_part:02d} UAH")

    def set_values(self, whole_part, fractional_part):
        self._whole_part = whole_part
        self._fractional_part = fractional_part

    def calculate_in_currency(self, currency):
        exchange_rates = {"USD": 38, "EUR": 40}
        rate = exchange_rates.get(currency, 1)
        total_uah = self._whole_part + self._fractional_part / 100
        total_currency = total_uah / rate
        return total_currency

    def decrease_price(self, decrease_whole, decrease_fractional):
        total_in_cents = self._whole_part * 100 + self._fractional_part
        decrease_total_in_cents = decrease_whole * 100 + decrease_fractional
        new_total_in_cents = max(0, total_in_cents - decrease_total_in_cents)
        self._whole_part = new_total_in_cents // 100
        self._fractional_part = new_total_in_cents % 100


class Product(Money):
    def __init__(self, whole_part, fractional_part, name):
        super().__init__(whole_part, fractional_part)
        self.name = name

    def get_product(self):
        print(f"{self.name} коштує: {self._whole_part}.{self._fractional_part:02d} UAH")

    def display_price_in_currencies(self):
        print(
            f"{self.name} коштує: {self.calculate_in_currency('USD'):.2f} у USD, {self.calculate_in_currency('EUR'):.2f} у EUR")


product = Product(39, 99, "Milk")
product.decrease_price(5, 50)
product.get_product()
product.display_price_in_currencies()


