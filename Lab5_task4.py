# Завдання 4
# Створіть базовий клас Clock, який містить атрибути
# години та хвилини. Від цього базового класу
# успадковуйте два класи: AnalogClock та DigitalClock.
# Клас AnalogClock повинен мати метод display_time,
# який виводить поточний час у форматі
# "години:хвилини". Клас DigitalClock повинен мати
# метод display_time, який виводить поточний час у
# цифровому форматі "гг:хх".
# Створіть об'єкти кожного класу та виведіть
# поточний час за допомогою методу display_time.
class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes


class AnalogClock(Clock):
    def display_time(self):
        print(f"{self.hours}:{self.minutes}")


class DigitalClock(Clock):
    def display_time(self):
        period = "am" if self.hours < 12 else "pm"
        hours_formatted = self.hours % 12 or 12
        print(f"{hours_formatted:02}:{self.minutes:02} {period}")


analog_clock = AnalogClock(15, 30)
digital_clock = DigitalClock(15, 30)


analog_clock.display_time()
digital_clock.display_time()
