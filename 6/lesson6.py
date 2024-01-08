# все, что даеться на уроке - повторяю ручками для лучшего понимания


class Box:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def __str__(self):
        return f'L - {self.length}, W = {self.width}, H - {self.height}'

    def __imul__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        self.length *= other
        self.width *= other
        self.height *= other
        return self

    def __mul__(self, other: int | float):
        if not isinstance(other, int | float):
            return NotImplemented
        return Box(self.length * other, self.width *
                   other, self.height * other)

    def __rmul__(self, other: int | float):
        if not isinstance(other, int | float):
            return NotImplemented
        return Box(self.length * other, self.width *
                   other, self.height * other)

    def __gt__(self, other):
        if isinstance(other, Box):
            return self.volume() > other.volume()
        elif isinstance(other, tuple):
            if len(other) != 3:
                return NotImplemented
            if not all(isinstance(i, (int, float)) for i in other):
                return NotImplemented
            x, y, z = other
            return self.volume() > x * y * z

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __eq__(self, other):
        return self.volume() == other.volume()

    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __ne__(self, other):
        return self.volume() != other.volume()


box_1 = Box(1, 2, 3)
box_2 = 3 * box_1
print(box_1)
print(box_2)
