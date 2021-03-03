# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]


# Data structure realisation:

string_counter = 0
dict_template = {"название": '', "цена": '', "количество": '', "единица измерения": ''}
tuple_template = (string_counter, dict_template)
product_list = []

item_quantity = int(input("Введите количество товаров, которые хотите добавить "))

while item_quantity <= 0:
    item_quantity = int(input("Введите количество товаров, которые хотите добавить "))

else:
    while string_counter < item_quantity:
        print("Введите " + str(string_counter + 1) + "-й товар")
        # create temple list as tuple, to modify it
        temp_list = list(tuple_template)

        # idk how to get key quantity, (i know, but it will make code unreadable) sorry for this sh*t
        dict_key_counter = 0
        while dict_key_counter < 4:
            # add key_value to dict keys
            temp_list[1].update({list(temp_list[1].keys())[dict_key_counter]: input(
                "Введите " + list(temp_list[1].keys())[dict_key_counter] + " ")})
            dict_key_counter += 1

        # create temp dict to save information
        temp_dict = dict(temp_list[1])
        # re-write temple list with needed product information and add string counter
        string_counter += 1
        temp_list = [string_counter, temp_dict]

        # create temple tuple to add it to products.
        temp_tuple = tuple(temp_list)
        product_list.append(temp_tuple)

print("\nВсе товары добавлены!")

for el in product_list:
    print(el)

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# Data analytic realisation:
new_dict = dict()
new_list = list()
dict_key_counter = 0

while dict_key_counter < 4:
    new_dict.update({list(product_list[0][1].keys())[dict_key_counter]: ''})
    dict_key_counter += 1

dict_key_counter = 0
temp_list.clear()
while dict_key_counter < 4:
    for el in range(len(product_list)):
        element = (product_list[el][1].get(list(product_list[el][1].keys())[dict_key_counter]))
        temp_list.append(element)
    final_list = temp_list.copy()
    new_dict.update({list(product_list[0][1].keys())[dict_key_counter]: final_list})
    dict_key_counter += 1
    temp_list.clear()

for keys, values in new_dict.items():
    print(keys, ':', values)