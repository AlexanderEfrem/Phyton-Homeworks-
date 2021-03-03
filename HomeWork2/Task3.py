#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input("Введите число от 1 до 12 "))
while number <= 0 or number > 12:
    number = int(input("Введите число от 1 до 12 "))

else:
    season_dict = {
        1: 'зима',
        2: 'весна',
        3: 'лето',
        4: 'осень'
    }

    if number == 1 or number == 2 or number == 12:
        print("Время года:", season_dict.get(1))

    elif 3 <= number <= 5:
        print("Время года:", season_dict.get(2))

    elif 6 <= number <= 8:
        print("Время года:", season_dict.get(3))

    elif 9 <= number <= 11:
        print("Время года:", season_dict.get(4))

#########################################################################

    season_list = [
        'зима',
        'весна',
        'лето',
        'осень'
    ]

    if number == 1 or number == 2 or number == 12:
        print("Время года:", (season_list[0]))

    elif 3 <= number <= 5:
        print("Время года:", (season_list[1]))

    elif 6 <= number <= 8:
        print("Время года:", (season_list[2]))

    elif 9 <= number <= 11:
        print("Время года:", (season_list[3]))