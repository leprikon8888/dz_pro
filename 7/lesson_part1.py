# повторное прохождение занятия, на след день, с прописью ручками
class CartIterator:
    def __init__(self, items, qty):
        self.__items = items
        self.__qty = qty
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__items):
            raise StopIteration()
        item = self.__items[self.__index]
        qty = self.__qty[self.__index]
        self.__index += 1
        return item, qty


class Cart:

    def __init__(self):
        self.__items = []
        self.__qty = []

    def add(self, item, qty=1):
        self.__items.append(item)
        self.__qty.append(qty)

    def __iter__(self):
        return CartIterator(self.__items, self.__qty)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__items[item], self.__qty[item]

    def __len__(self):
        return len(self.__items)

    def __iadd__(self, other: tuple):
        if isinstance(other, tuple):
            item, qty = None, 1
            if len(other) == 2:
                item, qty = other
            elif len(other) == 1:
                item = other[0]
            self.__items.append(item)
            self.__qty.append(qty)
            return self

        if isinstance(other, Cart):
            self.__items.extend(other.__items)
            self.__qty.extend(other.__qty)
            return self

        return NotImplemented

    def total(self):
        s = 0
        for item, qty in self:
            s += item.price * qty
        return s


if __name__ == '__main__':
    cart = Cart()
    cart.add('Apple', 10)
    cart.add('Cola', 5)
    cart.add('Kiwi', 3)
    cart.add('Banana', 7)

    for item, qty in cart:
        print(f'{item} - {qty}')
        
    print(cart[0])