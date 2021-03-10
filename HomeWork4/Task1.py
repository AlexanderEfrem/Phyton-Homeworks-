# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(workHours, rate, prize):
    result_salary = (int(workHours) * int(rate)) + int(prize)
    print("Заработная плата сотрудника = " + str(result_salary))

name, workHours, rate, prize = argv

salary(workHours, rate, prize)
