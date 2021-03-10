# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def find_min_and_remove(list):
    min = list[0]
    for el in list:
        if el < min:
            min = el
    list.remove(min)
    return list


def my_func(val1, val2, val3):
    errors = []
    if val1 == val2 and val1 == val3:
        errors.append("Нельзя найти наибольшее число")

    else:
        list = [val1, val2, val3]
        updated_list = find_min_and_remove(list)
        summ = sum(updated_list)

    if errors:
        return {
            'Статус': 'Ошибка',
            'сообщения': errors
        }
    else:
        return summ


number1 = int(input("Введите число 1 "))
number2 = int(input("Введите число 2 "))
number3 = int(input("Введите число 3 "))

summ = my_func(number1, number2, number3)

print("Сумма елементов = " + str(summ))
