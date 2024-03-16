"""
Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата.
"""
import math


def square(side):
    perimtr = 4 * side
    s = side ** 2
    diagonal = round((2 * side ** 2) ** 0.5, 2)

    # s = int(math.pow(side, 2))
    # diagonal = round(math.pow((2 * side ** 2), 0.5), 2)

    diagonal = round(math.sqrt(2 * side ** 2), 2)

    return (perimtr, s, diagonal)


n = int(input("Введите сторону квадрата:"))
print(square(n))
