import product
import user_error
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

terminal_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log.txt')

terminal_handler.setLevel(logging.DEBUG) # Записывать все сообщения уровня DEBUG и выше в терминал
file_handler.setLevel(logging.INFO)  # Записывать все сообщения уровня INFO и выше в файл

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
terminal_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(terminal_handler)
logger.addHandler(file_handler)


class Cart:
    logger = logging.getLogger(__name__)

    def __init__(self, max_carts=3):
        self.max_carts = max_carts
        self.products = []
        self.quantities = []

    def add_product(self, new_product: product.Product, quantity: int | float = 1):
        """
        Add product to cart.
        """
        if not isinstance(new_product, product.Product) or not isinstance(quantity, (int, float)):
            logger.error("Invalid type.")
            raise TypeError("Invalid type.")
        if len(self.products) == self.max_carts:
            logger.exception(f"Превышен лимит корзины ({self.max_carts} товаров)")
            raise user_error.CartLimitError(self.max_carts)
        self.products.append(new_product)
        self.quantities.append(quantity)

        logger.info(f"Добавлен продукт в корзину: {new_product.name} - {quantity}шт.")
    def total(self):
        return sum(prod.price * quan for prod, quan in zip(self.products, self.quantities))

    def __len__(self):
        return len(self.products)

    def __str__(self):
        res = f'{time.ctime()}: Items {len(self)}\n'
        for prod, quan in zip(self.products, self.quantities):
            res += f'{prod.name} - {prod.price} x {quan} = {prod.price * quan} UAH\n'
        res += f'Total: {self.total()} UAH'
        return res
