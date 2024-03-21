# Завдання 4
# Створіть клас FileUtils, який має метод класу
# count_lines, який приймає шлях до файлу і повертає
# кількість рядків у файлі.
class FileUtils:
    @classmethod
    def count_lines(cls, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return sum(1 for _ in file)
        except FileNotFoundError:
            print(f"Файл за шляхом '{file_path}' не знайдено.")
            return None
        except Exception as e:
            print(f"Сталася помилка при відкритті файлу: {e}")
            return None


file_path = 'file.txt'
line_count = FileUtils.count_lines(file_path)
if line_count is not None:
    print(f"Файл '{file_path}' містить {line_count} рядків.")

