# Модифицируйте первое домашнее задание (О заказе), добавив проверки в методы классов и обработку исключительных ситуаций.
# При попытке установить отрицательную или нулевую стоимость товара # следует вызвать исключительную ситуацию, тип
# которой реализовать # самостоятельно.

import time


class CartLimitError(Exception):
    def __init__(self, max_el, message='too many carts'):
        self.message = message
        self.max_el = max_el
        super().__init__(self.message)

    def __str__(self):
        return f'Limit of carts {self.max_el} \n  {self.message}'


class Product:
    """
    Product class.
    """

    def __init__(self, name: str, price: float | int):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


class Cart:
    """
    Cart class.
    """

    def __init__(self, max_carts=3):
        self.max_carts = max_carts
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float = 1):
        """
        Add product to cart.
        """
        if not isinstance(product, Product) or not isinstance(quantity, (int, float)):
            raise TypeError("Invalid type.")
        if len(self.products)== self.max_carts:
            raise CartLimitError(self.max_carts)
        self.products.append(product)
        self.quantities.append(quantity)

    def total(self):
        """        Calculate total price.
        """
        return sum(product.price * quantity for product,
                   quantity in zip(self.products, self.quantities))

    def __len__(self):
        return len(self.products)

    def __str__(self):
        res = f'{time.ctime()}: Items {len(self)}\n'
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product.name} - {product.price} x {quantity} = {product.price * quantity} UAH\n'
        res += f'Total: {self.total()} UAH'
        return res


if __name__ == '__main__':
    try:
        # Проверка создания продуктов
        product_1 = Product('Milk', 20)
        product_2 = Product('Bread', 10)
        product_3 = Product('Meat', 100)
        product_4 = Product('kiwi', 301)

    except Exception as e:
        print('Ошибка при создании продуктов:', e)
    else:
        try:
            # Проверка добавления продуктов в корзину
            cart = Cart()
            cart.add_product(product_1, 2)
            cart.add_product(product_2)
            cart.add_product(product_3, 1.5)
            cart.add_product(product_4, 3)

            print(cart)
        except CartLimitError as e:
            print('Превышен лимит покупок:', e)
        except TypeError as e:
            print('Ошибка добавления продукта в корзину:', e)
