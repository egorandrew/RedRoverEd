"""
Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
"""
from functools import reduce

my_list = [20, -3, 15, 2, -1, -21]
proiz = reduce(lambda x, y: x * y, my_list)

print(proiz)
print(reduce(lambda x, y: x * y, my_list))
