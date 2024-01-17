'''Создайте класс "Счет", обладающий приватным свойством "баланс". Используйте специальные методы для контроля доступа к
этому свойству. Добавьте свойство balance с декоратором @property, которое возвращает значение баланса. Определите метод
__setattr__, запрещающий непосредственное изменение значения баланса. Также определите метод __getattr__, возвращающий
сообщение о том, что свойство не существует, если доступ к нему попытаться получить. Используйте этот класс для
создания объекта счета и попробуйте изменить значение баланса и получить доступ к несуществующему свойству.'''


class Receipt:

    def __init__(self, balance = 0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def __setattr__(self, key, value):
        if key == 'balance':
            raise AttributeError('нельзя устанавливать значения')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        raise AttributeError('нет такого атрибута')

x = Receipt(100)
print(x.balance)
x.total = 200
print(x.file)