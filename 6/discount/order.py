import logging
import discount
import product


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

terminal_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log.txt')

terminal_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
terminal_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(terminal_handler)
logger.addHandler(file_handler)


class Customer:
    def __init__(self, name: str, disc: 'discount.Discount'):
        try:
            if not isinstance(name, str):
                raise TypeError("Имя должно быть строкой")
            if not isinstance(disc, discount.Discount):
                raise TypeError("Скидка должна быть объектом класса Discount")
            self.name = name
            self.discount = disc
        except Exception as e:
            logger.exception("Ошибка при создании объекта Customer")


class Order:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, prod: 'product.Product', quantity: int):
        try:
            if not isinstance(prod, product.Product):
                raise TypeError("prod должен быть объектом класса Product")
            if not isinstance(quantity, int):
                raise TypeError("quantity должно быть целым числом")
            self.products.append(prod)
            self.quantities.append(quantity)
        except Exception as e:
            logger.exception("Ошибка при добавлении продукта в заказ")

    def __iadd__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            prod, quantity = other
            if isinstance(product, product.Product) and isinstance(quantity, int):
                self.add_product(prod, quantity)
                return self
        elif isinstance(other, product.Product):
            self.add_product(other, 1)
            return self
        raise ValueError("Неверный формат для добавления продукта в заказ")

    def total_price(self, customer: Customer = None):
        try:
            if customer and not isinstance(customer, Customer):
                raise TypeError(
                    "customer должен быть объектом класса Customer")
            disc = customer.discount.discount() if customer and hasattr(
                customer, 'discount') else 0
            total = 0
            for prod, quan in zip(self.products, self.quantities):
                total += prod.price * quan
            return total * (1 - disc)
        except Exception as e:
            logger.exception("Ошибка при расчете общей стоимости заказа")
