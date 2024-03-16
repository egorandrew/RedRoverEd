"""
Напишите программу, которая определяет, какая семья больше.
1) Программа имеет два input() - например, family_1, family_2.
2) Членов семьи нужно перечислить через запятую.
Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
"""
family_1 = tuple(input("Введите членов первой семьи:").split(","))
family_2 = tuple(input("Введите членов второй семьи:").split(","))
if len(family_1) > len(family_2):
    print("Большая семья:", family_1)
elif len(family_1) < len(family_2):
    print("Большая семья:", family_2)
else:
    print("Equal")
