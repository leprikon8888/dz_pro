'''Создайте класс "Пользователь", который имеет свойства first_name и last_name. Используйте декораторы @property для
обеспечения доступа к этим свойствам. Определите метод __setattr__, запрещающий непосредственное изменение значений
first_name и last_name. Используйте метод __getattr__, который возвращает сообщение о том, что свойство не существует,
если попытаться получить доступ к несуществующему свойству. Создайте пользовательский объект и попробуйте изменить
значение first_name и получить доступ к несуществующему свойству.'''

class User:

    def __init__(self, name, last_name):
        self.__first_name = name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name


    def __setattr__(self, key, value):
        if key in ('first_name', 'last_name'):
            raise AttributeError ('нельзя менять')
        else:
            object.__setattr__(self,key,value)


    def __getattr__(self, item):
        return 'No such attribute '
