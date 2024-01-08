'''Task 1
Предыдущий проект (Заказ продуктов в магазине) дополнить итерационным протоколом.'''


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'just {self.name}, price = {self.price}'


pr_1 = Product('apple', 3, 'fresh fruit')
pr_2 = Product('kola', 6, 'drink')
pr_3 = Product('oreo', 5, 'snack')
pr_4 = Product('kiwi', 7, 'green fruit')


class Cart:
    def __init__(self, name):
        self.products = []
        self.name = name
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            res = self.products[self.index]
            self.index +=1
            return res
        else:
            raise StopIteration

    def add_basket(self, product: Product):
        if isinstance(product, Product):
            self.products.append(product)

    def __str__(self):
        return f'{self.name}: \n{"\n".join(map(str, self.products))}'

basket = Cart('My Basket')
basket.add_basket(pr_4)
basket.add_basket(pr_3)
basket.add_basket(pr_1)
basket.add_basket(pr_2)


for i in basket:
    print (i)

