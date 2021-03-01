#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

value1 = (input("Введите число: "))
value2 = str(value1) + str(value1)
value3 = str(value2) + str(value1)
value_final = (int(value1)+ int(value2) + int(value3))

print("Cумма чисел n + nn + nnn =",value_final)