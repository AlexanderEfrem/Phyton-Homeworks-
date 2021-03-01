#2. Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
seconds = 0

while seconds <= 0:
    seconds = int(input('Введите время в секундах: '))
    if seconds <= 0:
        print("Введенное время меньше, либо равно 0")

    else:
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        break

