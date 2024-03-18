# Реалізуйте клас «Вебсайт». Збережіть у класі: назву
# вебсайту, адресу та опис вебсайту. Реалізуйте конструктор
# та методи класу для введення-виведення даних, а також
# для інших операцій. Використовуйте механізм перевантаження методів.
import re
class Website:
    def __init__(self, name="", url="", description=""):
        self.name = name
        self.url = url
        self.description = description

    def input_data(self):
        self.name = input("Введіть назву вебсайту: ")
        url_pattern = re.compile(r'^https?:\/\/[\w\-\.]+\.\w{2,5}$')
        while True:
            temp_url = input(
                "Введіть адресу вебсайту (мусить починатись з http:// або https:// та закінчуватись на .домен): ")
            if url_pattern.match(temp_url):
                self.url = temp_url
                break
            else:
                print("Адреса вебсайту не відповідає необхідному формату. Будь ласка, спробуйте ще раз.")
        self.description = input("Введіть опис вебсайту: ")

    def display_data(self):
        print("\nІнформація про вебсайт:")
        print(f"Назва: {self.name}")
        print(f"Адреса: {self.url}")
        print(f"Опис: {self.description}")

    def __eq__(self, other):
        return self.url == other.url
    def __lt__(self, other):
        return self.name < other.name
    def __str__(self):
        return f"Вебсайт: {self.name}, Адреса: {self.url}, Опис: {self.description}"

website1 = Website()
website2 = Website()

website1.input_data()
website1.display_data()

website2.input_data()
website2.display_data()

if website1.name == website2.name:
    print("Назви сайтів однакові.")
else:
    print("Назви сайтів різні.")
if website1.url == website2.url:
    print("Адреси сайтів одникові.")
else:
    print("Адреси сайтів різні.")

print(website1)
print(website2)
