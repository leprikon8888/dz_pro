'''Создайте класс "Правильная Дробь" и реализуйте методы сравнения, сложения, вычитания и умножения для экземпляров
этого класса. Не забудьте про сокращение дроби.'''
import math


class Fraction:
    def __init__(self, numerator, denominator):
            if not isinstance(numerator, int):
                raise TypeError('Numerator must be an integer')
            if not isinstance(denominator, int):
                raise TypeError('Denominator must be an integer')
            if denominator ==0:
                raise ValueError('Denominator cannot be zero')
            self.numerator = numerator
            self.denominator = denominator


    def __add__(self, other):
        if isinstance(other, Fraction):
            new_denominator = self.denominator * other.denominator
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            return Fraction(new_numerator, new_denominator)

        if isinstance(other, int):
            numerator = self.numerator + other * self.denominator
            return  Fraction(numerator, self.denominator)

        raise  TypeError ('Data type error')

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator


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


    def __str__(self):
        tmp = math.gcd(self.numerator, self.denominator)
        self.numerator //= tmp
        self.denominator //= tmp
        sign = '-' if self.numerator * self.denominator < 0 else ''
        numerator = abs(self.numerator)
        denominator = abs(self.denominator)
        if denominator ==1:
            return f'{sign}{numerator}'
        if numerator == 0:
            return '0'
        if numerator == denominator:
            return f'{sign}1'
        if numerator > denominator:
            integer = numerator // denominator
            numerator %= denominator
            return f'{sign}{integer} {numerator}/{denominator}'

        return f'{sign}{numerator}/{denominator}'


a = Fraction(-25, 10)
b = Fraction(13, 11)
# c = Fraction(325, 100)
# d = Fraction(325, 100)
c = a *b

print(a)
print(b)
print(c)