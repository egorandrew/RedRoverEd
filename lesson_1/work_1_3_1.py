"""
Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
"""
number = int(input("Введите 4-х значное число:"))
print(f"Тысячи-{number//1000}")
print(f"Сотни-{number % 1000//100}")
print(f"Десятки-{number % 100 // 10}")
print(f"Единицы-{number % 10}")