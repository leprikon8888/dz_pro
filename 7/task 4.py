'''Реализуй свой аналог генераторной функции range().'''

def my_range(*args):
    if not all(isinstance(item, int) for item in args):
        raise TypeError('we need  integers in args')
    start, stop, step = 0, None, 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise ValueError('we need 3 arguments')

    if step == 0:
        raise ValueError

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

for i in my_range(40, 20, -1):
    print(i)