"""
Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
"""

import time
from functools import reduce


def my_decorator(func):
    def wapper(*args):
        old_time = time.perf_counter()
        old_time_2 = time.time()
        print(old_time)
        result = func(*args)
        new_time = time.perf_counter()
        new_time_2 = time.time()
        print(new_time)
        print(f"Время выполнения функции {func.__name__} {new_time - old_time}")
        print(f"Время выполнения функции {func.__name__} {new_time_2 - old_time_2}")
        return result

    return wapper


@my_decorator
def how_time_1(massiv):
    time.sleep(1)
    proiz = sum(filter(lambda x: x % 2, massiv))
    return proiz


@my_decorator
def how_time_2(massiv):
    time.sleep(1)
    proiz = 0
    for i in massiv:
        if i % 2:
            proiz += i
    return proiz


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = how_time_1(my_list)
print(f"Результат: {a}")
b = how_time_2(my_list)
print(f"Результат: {b}")
