"""
Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
производит заданное арифметическое действие и печатает результат в формате:
{num1} {operator) {num2) = {result}
"""
num_1 = float(input("Введите  число 1:"))
num_2 = float(input("Введите  число 2:"))
operator = input("Введите один из операторов '+', '-', '*', '/':")
result = None
if operator == "+":
    result = num_1 + num_2
elif operator == "-":
    result = num_1 - num_2
elif operator == "*":
    result = num_1 * num_2
elif operator == "/":
    if num_2 == 0:
        print("На ноль делить нельзя.")
    else:
        result = num_1 / num_2
else:
    print("Не существующий оператор")
if result is not None:
    print(f"{num_1} {operator} {num_2} = {result}")
