'''Task 3
Реализуйте генераторную функцию, возвращающую по одному члену геометрической прогрессии.'''


def geom_generation(start, x):
    while True:
        yield start
        start *= x


for i in geom_generation(2,3):
    print(i)
    if i > 200000:
        break