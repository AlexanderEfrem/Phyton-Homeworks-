# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_list = input().split()

for el in user_list:
    second_list = list(el)
    symbol_limit = 10

    if len(second_list) > symbol_limit:
        del second_list[symbol_limit:len(second_list)]
        string = ""
        for ele in second_list:
            string += ele

        print("Строка №" + str(user_list.index(el)) + " слово: " + string)

    else:
        print("Строка №" + str(user_list.index(el)) + " слово: " + el)
