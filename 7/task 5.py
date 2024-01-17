'''Напишите генераторную функцию, которая возвращает простые числа. Верхний предел диапазона должен быть задан
параметром этой функции.'''


def my_generator_rational_integer(stop):
    for number in range(2, stop):
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            yield number

for num in my_generator_rational_integer(100):
    print(num)