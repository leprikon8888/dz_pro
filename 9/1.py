'''Створіть абстрактний базовий клас "Фігура" і від нього успадкуйте конкретні класи, такі як "Коло", "Прямокутник",
 "Трикутник" і т.д. Кожен клас має мати методи для обчислення площі та периметру фігури. Створіть декілька об'єктів
 різних фігур і виведіть їх площу та периметр.'''
from abc import ABC, abstractmethod
import math


class Figura(ABC):

    @abstractmethod
    def perimetr(self):
        ...

    @abstractmethod
    def area(self):
        ...


class Kolo(Figura):
    def __init__(self, radius):
        self.radius = radius

    def perimetr(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rect(Figura):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def perimetr(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Triangle(Figura):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimetr(self):
        return self.a + self.b + self.c

    def area(self):
        x = (self.a + self.b + self.c) / 2
        return math.sqrt(x * (x - self.a) * (x - self.b) * (x - self.c))


if __name__ == "__main__":

    a = Kolo(5)
    print(a.perimetr())
    print(a.area())

    b = Rect(2, 5)
    print(b.perimetr())
    print(b.area())

    c = Triangle(3, 7, 9)
    print(c.perimetr())
    print(c.area())
