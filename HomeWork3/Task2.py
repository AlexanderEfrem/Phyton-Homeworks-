#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
import datetime

def toString(firstName, lastName, dob, city, email, phone):
    str = " "
    list = [firstName, lastName, dob, city, email, phone]
    return str.join(list)

name = input("Введите имя ")
lName = input("Введите фамилию ")
dob = input("Введите дату рождения ")
city = input("Введите город проживания ")
email = input("Введите email ")
phone = input("Введите телефон ")

result = toString(name, lName, dob, city, email, phone)

print(result)