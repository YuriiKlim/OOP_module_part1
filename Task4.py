# Завдання 4
# До вже реалізованого класу «Книга» додайте
# необхідні перевантажені методи та оператори.
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.genre == other.genre

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.title < other.title

    def __le__(self, other):
        return self.title <= other.title

    def __gt__(self, other):
        return self.title > other.title

    def __ge__(self, other):
        return self.title >= other.title


book1 = Book("Гаррі Поттер і Філософський камінь", "Дж.К. Ролінг", "Фентезі")
book2 = Book("Володар Перснів", "Дж.Р.Р. Толкін", "Фентезі")
book3 = Book("Гаррі Поттер і Філософський камінь", "Дж.К. Ролінг", "Фентезі")

print(f"\n1:{book1}\n2:{book2}\n3:{book3}")

print(book1 == book3)
print(book1 == book2)

if book1 < book2:
    print(f"\"{book1.title}\" йде перед \"{book2.title}\" у алфавітному порядку.")
else:
    print(f"\"{book2.title}\" йде перед \"{book1.title}\" у алфавітному порядку.")
