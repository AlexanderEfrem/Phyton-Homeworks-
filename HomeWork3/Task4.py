# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    if x == 0:
        return 0

    if y == 0 or x == 1:
        return 1

    else:
        xInY = x
        while y != -1:
            xInY *= x
            y += 1
        result = 1 / xInY
    return result


number1 = float(input("Введите дейтвительное число : "))

number2 = 0
while number2 >= 0:
    number2 = int(input("Введите отрицательное целое число: "))

result = my_func(number1, number2)
print(result)
