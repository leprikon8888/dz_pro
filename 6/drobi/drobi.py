'''Создайте класс "Правильная Дробь" и реализуйте методы сравнения, сложения, вычитания и умножения для экземпляров
этого класса. Не забудьте про сокращение дроби.'''
import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        # Находим наибольший общий делитель
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd  # Сокращаем числитель
        self.denominator = self.denominator // gcd  # Сокращаем знаменатель

    def __str__(self):
        whole = self.numerator // self.denominator
        remainder = self.numerator % self.denominator

        if remainder == 0:
            return str(whole)
        elif whole == 0:
            return f"{self.numerator}/{self.denominator}"
        else:
            return f"{whole}  {remainder}/{self.denominator}"

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __add__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + \
            (other.numerator * self.denominator)
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) - \
            (other.numerator * self.denominator)
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)


a = Fraction(25, 10)
b = Fraction(13, 10)
c = Fraction(325, 100)
d = Fraction(325, 100)

print(c==d)
print(c>d)
print(a * b)
print(c)

print((a*b) == c)