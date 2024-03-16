"""
Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
- получите сумму всех чисел,
- распечатайте все строки, где есть буква 'a'
"""
list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
summ = []
slovo = ""
for i in list_1:
    if type(i) is int:
        summ.append(i)
    else:
        if "a" in i:
            print(i)
        else:
            pass
print(sum(summ))
print([x for x in list_1 if isinstance(x, str) and 'a' in x])
