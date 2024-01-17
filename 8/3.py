'''Создайте класс "Прямоугольник", имеющий приватные свойства width и height. Используйте декораторы @property для
создания свойств width и height, возвращающих значение этих свойств. Определите метод __setattr__, запрещающий
непосредственное изменение значений width и height. Используйте метод __getattr__, который возвращает сообщение о том,
что свойство не существует, если попытаться получить доступ к несуществующему свойству. Добавьте метод area, вычисляющий
площадь прямоугольника. Создайте объект прямоугольника и попытайтесь изменить значения width и height, а также получить
доступ к несуществующему свойству и вычислить площадь прямоугольника.'''


class Rect:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height


    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def __setattr__(self, key, value):
        if key == 'width' or key == 'height':
            raise AttributeError('нельзя менять эти свойства')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        raise AttributeError('no such attribute')

    def area(self):
        return self.width*self.height

a = Rect(3,4)
print(a.width)
print(a.area())
