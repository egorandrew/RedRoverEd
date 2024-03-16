"""
Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
в формате аргумент: значение. Например:
name: John
last_name: Smith
age: 35
position: web developer
"""


def my_function(**kwargs):
    for name, value in kwargs.items():
        print(f'{name}: {value}')


my_function(name="John", last_name="Smith", age=35, position="web developer")
