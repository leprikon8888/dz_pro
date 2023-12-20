"""Task 1
Создайте класс Product для описания продукта (товара). В качестве атрибутов продукта можно употреблять название, цену и
описание. Создайте несколько инстансов класса Product. Создайте класс Cart, который будет выступать в качестве корзины с
 продуктами определенного покупателя. Корзина может содержать несколько продуктов определенного количества. Реализуйте
 метод вычисления стоимости корзины. Во всех классах должен быть определен метод str.
"""


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'just {self.name}'


pr_1 = Product('apple', 3, 'fresh fruit')
pr_2 = Product('kola', 6, 'drink')
pr_3 = Product('oreo', 5, 'snack')
pr_4 = Product('kiwi', 7, 'green fruit')


class Cart:
    def __init__(self, name):
        self.products = []
        self.name = name

    def add_basket(self, product: Product):
        if isinstance(product, Product):
            self.products.append(product)

    def total_price(self):
        res = 0
        for i in self.products:
            res += i.price
        return res

    def __str__(self):
        return f'{self.name}: \n{"\n".join(map(str, self.products))}'

basket = Cart('My Basket')
basket.add_basket(pr_4)
basket.add_basket(pr_3)
basket.add_basket(pr_1)
print(basket)
print(basket.total_price())
