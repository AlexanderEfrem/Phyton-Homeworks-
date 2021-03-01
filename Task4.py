#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции..
value = 0

while value <=0:
    value = int(input("Введите целое положительно число "))
    if value <=0:
        value = int(input("Введите целое положительно число "))

    else:
        string = str(value)
        index = 0
        maxValue = 0

        while int(string[index]) > int(maxValue):
            maxValue = string[index]
            index = index + 1
            if (index >= len(string)):
                print("Максимальное число = ", maxValue)
                exit()

    print("Максимальное число = ", maxValue)












