"""Task 2
Необходимо разработать Python-скрипт, возвращающий пользователю меню ресторана. Обычно меню ресторана содержит следующие
 элементы:
- категории блюд (например, закуски, основные блюда, десерты).
- блюда в каждой категории.
Основные классы, которые необходимо создать для реализации меню ресторана:
Класс Блюдо: отвечает за сохранение информации об отдельном блюде, включая его название, описание и цену.
Класс Категория блюд: отвечает за сохранение блюд, относящихся к конкретной категории. Включает список объектов Блюдо.
"""


class Dish:
    def __init__(self, name, price, descr):
        self.name = name
        self.descr = descr
        self.price = price

    def __str__(self):
        return f'{self.name} | {self.descr}, стоит => {self.price} условных единиц'


class Category:
    def __init__(self, title):
        self.title = title
        self.dishes = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def __str__(self):
        return f'Категория {self.title} содержит следующие блюда:\n{"\n".join(map(str, self.dishes))}\n{50 * "*"}\n'


class Menu:
    def __init__(self, title):
        self.title = title
        self.menu = []

    def add_category(self, category: Category):
        self.menu.append(category)

    def __str__(self):
        return f'{self.title} содержит следующие категории блюд:\n\n{"\n".join(map(str, self.menu))}'


coffee = Dish('coffee', 40, 'hot drink')
tea = Dish('tea', 60, 'hot drink')
juice = Dish('coffee', 35, 'hot drink')

pancake = Dish('pancake', 30, 'desert')
baked_pudding = Dish('baked pudding', 60, 'запеканка')
cherry_pie = Dish('cherry_pie', 70, 'вишневый пирог')

beef_steak = Dish('beef_steak', 140, 'бифштекс')
hamburger = Dish('hamburger', 120, 'гамбургер')
roast = Dish('roast', 130, 'жаркое')


drinks = Category('Drinks')
drinks.add_dish(coffee)
drinks.add_dish(tea)
drinks.add_dish(juice)

deserts = Category('Deserts')
deserts.add_dish(pancake)
deserts.add_dish(baked_pudding)
deserts.add_dish(cherry_pie)

the_main_course = Category('The main course')
the_main_course.add_dish(beef_steak)
the_main_course.add_dish(hamburger)
the_main_course.add_dish(roast)

menu = Menu('Menu')
menu.add_category(drinks)
menu.add_category(deserts)
menu.add_category(the_main_course)


print(menu)
