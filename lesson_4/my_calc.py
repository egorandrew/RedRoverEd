def pluc(a, b):
    return a + b


def minus(a, b):
    return a - b


def umnogenie(a, b):
    return a * b


def delenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "На ноль делить нельзя"


