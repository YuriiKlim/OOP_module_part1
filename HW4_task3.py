# Завдання 3
# Створіть клас для конвертування з метричної системи в
# англійську, та навпаки. Реалізуйте функціональність у вигляді
# статичних методів. Обов’язково реалізуйте конвертування
# заходів довжини.
class MetricToImperialConverter:
    conversion_count = 0
    @staticmethod
    def meters_to_feet(meters):
        MetricToImperialConverter.conversion_count += 1
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        MetricToImperialConverter.conversion_count += 1
        return feet / 3.28084

    @staticmethod
    def centimeters_to_inches(centimeters):
        MetricToImperialConverter.conversion_count += 1
        return centimeters * 0.393701

    @staticmethod
    def inches_to_centimeters(inches):
        MetricToImperialConverter.conversion_count += 1
        return inches / 0.393701

    @staticmethod
    def get_conversion_count():
        return MetricToImperialConverter.conversion_count


meters = 1
feet = MetricToImperialConverter.meters_to_feet(meters)
print(f"{meters:g} meter(s) is {feet:g} foot(s)")

feet = 1
meters = MetricToImperialConverter.feet_to_meters(feet)
print(f"{feet:g} foot(s) is {meters:g} meter(s)")

centimeters = 1
inches = MetricToImperialConverter.centimeters_to_inches(centimeters)
print(f"{centimeters:g} centimeter(s) is {inches:g} inch(es)")

inches = 1
centimeters = MetricToImperialConverter.inches_to_centimeters(inches)
print(f"{inches:g} inch(es) is {centimeters:g} centimeter(s)")

print(f"Total conversions done: {MetricToImperialConverter.get_conversion_count()}")
