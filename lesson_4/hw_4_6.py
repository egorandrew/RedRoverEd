"""
Создайте файл my_calc.py и пропишите в нем минимум 4 функции,
выполняющие базовые арифметические вычисления.
Примените эти функции в качестве методов в другом файле.
"""
import my_calc

num_1 = float(input("Введите  число 1:"))
num_2 = float(input("Введите  число 2:"))
result_1 = my_calc.pluc(num_1, num_2)
print(result_1)
result_2 = my_calc.minus(num_1, num_2)
print(result_2)
result_3 = my_calc.umnogenie(num_1, num_2)
print(result_3)
result_4 = my_calc.delenie(num_1, num_2)
print(result_4)