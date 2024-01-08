import cart
import product
import user_error

if __name__ == '__main__':
    try:
        # Проверка создания продуктов
        product_1 = product.Product('Milk', 20)
        product_2 = product.Product('Bread', 10)
        product_3 = product.Product('Meat', 100)
        product_4 = product.Product('kiwi', 301)

        # Создание объекта корзины
        cart_1 = cart.Cart()
        cart_2 = cart.Cart()
    except Exception as e:
        cart.logger.exception('Ошибка при создании продуктов:', e)
    else:
        try:
            # Проверка добавления продуктов в корзину
            cart_1.add_product(product_1, 2)
            cart_1.add_product(product_2)
            cart_1.add_product(product_3, 1.5)
            cart_2.add_product(product_1, 3)
            cart_2.add_product(product_4, 3)

            print(cart_1)
            print(cart_2)
            cart_1 += cart_2
            print(cart_1)
        except user_error.CartLimitError as e:
            cart.logger.exception('Превышен лимит покупок:')
        except TypeError as e:
            cart.logger.exception('Ошибка добавления продукта в корзину:', e)

