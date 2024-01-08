'''Task 2
Предыдущий проект (Меню Ресторана) дополнить итерационным протоколом и протоколом последовательности.'''

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
        self.index = 0

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dishes):
            result = self.dishes[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.dishes[index]

    def __len__(self):
        return len(self.dishes)

    def __str__(self):
        return f'Категория {self.title} содержит следующие блюда:\n{"\n".join(map(str, self.dishes))}\n{50 * "*"}\n'


class Menu:
    def __init__(self, title):
        self.title = title
        self.menu = []
        self.index = 0

    def add_category(self, category: Category):
        self.menu.append(category)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.menu):
            result = self.menu[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.menu[index]

    def __len__(self):
        return len(self.menu)

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


# print(menu)
# for i in drinks:
#     print(i)

#
# for i in menu:
#     print(i.title)

print(drinks[1])
print(len(menu))