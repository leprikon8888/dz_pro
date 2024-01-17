'''Реализуйте генераторную функцию для генерации последовательности дат. Начальная и конечная дата должны быть заданы
параметрами этой функции.'''

from datetime import datetime
from datetime import timedelta


def date_gen(start_date, end_date, step=1):
    while end_date >= start_date:
        yield start_date.strftime('%d-%m-%Y')
        start_date += timedelta(days=step)


start_date = datetime(2024, 1, 16)
end_date = datetime(2024,3, 1)

for date in date_gen(start_date, end_date):
    print(date)