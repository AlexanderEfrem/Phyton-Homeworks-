#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

element_quantity = int(input("Введите количество элементов списка "))

while element_quantity <= 0:
    element_quantity = int(input("Введите количество элементов списка "))

else:
    new_list = []
    counter = 0

    while counter < element_quantity:
        new_element = input("Введите " + str(counter) + "-й элемент списка ")
        new_list.append(new_element)
        counter += 1

    else:
        print("Ваш список до изменений: ", new_list)

        i = 0
        while i < len(new_list) - 1:
            new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
            i += 2

        else:
            print("Ваш список после изменений: ", new_list)


