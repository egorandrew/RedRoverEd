"""
Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
"""

my_list = ['a', 'b', [1, 2, 3], 'd']
massiv = []
for i in my_list:
    if type(i) is list:
        massiv = i
    else:
        pass
print(str(massiv).strip("[]"))
print(str(massiv)[1:-1])
print(", ".join(map(str, massiv)))
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])