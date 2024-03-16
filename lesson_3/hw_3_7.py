"""
Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
"""
a = [1, 2, 3, 4, 5, 3, 2, 1]
d = []
for i in a:
    if i not in d:
        d.append(i)
print(d)
print(list(dict.fromkeys(a)))
print(set(a))

