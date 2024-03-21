# Завдання 6
# Створіть клас Student, який має атрибути name, age,
# grade та courses. Реалізуйте метод класу add_course, який
# додає новий предмет до списку курсів студента
class Student:
    def __init__(self, name, age, grade, courses=None):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = courses if courses is not None else []

    def add_course(self, new_course):
        if new_course not in self.courses:
            self.courses.append(new_course)
            print(f"Курс '{new_course}' успішно додано до списку курсів {self.name}.")
        else:
            print(f"Курс '{new_course}' вже є в списку курсів {self.name}.")

student1 = Student("Юрій", 24, 2)
student1.add_course("Математика")
student1.add_course("Програмування")
student1.add_course("Математика")

print(f"Курси студента {student1.name}: {student1.courses}")
