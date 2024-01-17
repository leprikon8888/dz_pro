'''Реализуйте генераторную функцию, возвращающую элементы последовательности чисел Фибоначчи.'''


def fib_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

for i in fib_generator():
    print(i)
    if i >1000:
        break