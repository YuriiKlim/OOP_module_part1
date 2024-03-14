class Complex_Number:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex_Number(self.real + other.real, self.imag + other.imag)

num1 = Complex_Number(1, 2)
num2 = Complex_Number(3, 4)
result = num1 + num2
print(result)
