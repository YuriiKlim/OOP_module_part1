# Завдання 3
# Створіть клас Book з атрибутами title (назва
# книги), author (автор) та genre (жанр). Додайте метод
# display_info, який виведе інформацію про книгу у
# вигляді "Назва: {title}, Автор: {author}, Жанр: {genre}".



class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre =genre

    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}")

book1 = Book("Над зозуленим гніздом", "Кен Кізі", "Роман")
book1.display_info()

