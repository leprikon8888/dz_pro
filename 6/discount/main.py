import discount as discount_module
import product
import order as order_module
import logging

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

# Остальной код main.py...

discounts = {
    'regular': discount_module.RegularDiscount(),
    'silver': discount_module.SilverDiscount(),
    'gold': discount_module.GoldDiscount(),
    'platinum': discount_module.PlatinumDiscount(),
}

if __name__ == '__main__':
    print('Welcome to our shop!')
    print('Available discounts:')
    for disc in discounts:
        print(disc)

    while True:
        discount_choice = input('Please choose discount: ')
        if discount_choice in discounts:
            break
        else:
            print('Invalid discount choice. Please choose from the available discounts.')

    # Логирование выбранной скидки
    logger.info(f"Chosen discount: {discount_choice}")

    customer = order_module.Customer('John', discounts[discount_choice])

    product1 = product.Product('banana', 100)
    product2 = product.Product('apple', 200)
    customer_order = order_module.Order()
    customer_order.add_product(product1, 2)
    customer_order.add_product(product2, 1)

    total_price = customer_order.total_price(customer)

    # Логирование общей суммы заказа
    logger.info(f"Total price for the order: {total_price}")
    print(total_price)
