"""чем дальше - тем хуже справляюсь с базовыми домашками"""


class Discount:
    def discount(self, price):
        return price


class RegularDiscount(Discount):
    def discount(self, price):
        return price * 0.95


class SilverDiscount(Discount):
    def discount(self, price):
        return price * 0.93


class GoldDiscount(Discount):
    def discount(self, price):
        return price * 0.9


class Client:
    def __init__(self, name, discount: Discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        return f'Сумма заказа , без учета скидки - {order} \n' \
               f'Сумма заказа с учетом скиди - {self.discount.discount(order)}'


cl_1 = Client('Sasha', GoldDiscount())
cl_2 = Client('Sasha', SilverDiscount())
print(cl_1.get_total_price(200))
print(cl_2.get_total_price(200))