#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(val1, val2):
    errors = []
    if val2 == 0:
        errors.append("На ноль делить нельзя")
    else:
        c = val1 / val2

    if errors:
        return {
            'Статус' : 'Ошибка',
            'сообщения': errors
        }
    return c



number1 = int(input("Введите число 1: "))
number2 = int(input("Введите число 2: "))
number3 = div(number1, number2)
print("Результат деления = " + str(number3))
