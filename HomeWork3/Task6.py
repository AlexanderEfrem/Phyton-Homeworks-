#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(word):
    list1 = list(word)
    list1[0] = list1[0].upper()
    string = ""
    string = string.join(list1)
    return string

#Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func2():
    new_list = input("Введите строку cлов, разделенных пробелом. Q для выхода ").split()
    updated_list = []
    updated_string = " "
    for el in new_list:
        if el == 'Q':
            print(updated_list)
            exit()
        else:
            updated_word = int_func(el)
            updated_list.append(updated_word)
    updated_string = updated_string.join(updated_list)
    print("Исходная строка, но каждое слово начинается с заглавной буквы: " + updated_string)

int_func2()